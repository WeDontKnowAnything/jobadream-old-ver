import time
import copy
import yaml
import requests
import json
import os
import pandas as pd
from collections import namedtuple
from datetime import datetime, timedelta
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from base64 import b64decode
from typing import Dict, Any

# 콘솔을 클리어하는 함수
clear_console = lambda: os.system("cls" if os.name in ("nt", "dos") else "clear")

KEY_BYTES = 32
CONFIG_ROOT = "##"  # 토큰 파일이 저장될 폴더
TOKEN_TMP = CONFIG_ROOT + "KIS" + datetime.today().strftime("%Y%m%d")

# 접근 토큰 관리하는 파일 존재여부 체크, 없으면 생성
if not os.path.exists(TOKEN_TMP):
    with open(TOKEN_TMP, "w+"):
        pass

# 앱키, 앱시크리트, 토큰, 계좌번호 등 저장 관리
with open(CONFIG_ROOT + "kis_devlp.yaml", encoding="UTF-8") as f:
    _cfg = yaml.load(f, Loader=yaml.FullLoader)

_TRENV = namedtuple(
    "KISEnv", ["my_app", "my_sec", "my_acct", "my_prod", "my_token", "my_url"]
)
_last_auth_time = datetime.now()
_auto_reauth = False
_debug = False
_is_paper = False

# 기본 헤더값 정의
_base_headers = {
    "Content-Type": "application/json",
    "Accept": "text/plain",
    "charset": "UTF-8",
    "User-Agent": _cfg["my_agent"],
}


# 토큰을 저장하는 함수
def save_token(my_token: str, my_expired: str) -> None:
    valid_date = datetime.strptime(my_expired, "%Y-%m-%d %H:%M:%S")
    with open(TOKEN_TMP, "w", encoding="utf-8") as f:
        f.write(f"token: {my_token}\n")
        f.write(f"valid-date: {valid_date}\n")


# 토큰을 읽어오는 함수
def read_token() -> Any:
    try:
        with open(TOKEN_TMP, encoding="UTF-8") as f:
            token_data = yaml.load(f, Loader=yaml.FullLoader)

        exp_dt = datetime.strftime(token_data["valid-date"], "%Y-%m-%d %H:%M:%S")
        now_dt = datetime.today().strftime("%Y-%m-%d %H:%M:%S")

        if exp_dt > now_dt:
            return token_data["token"]
        else:
            return None
    except Exception as e:
        return None


# 기본 헤더를 가져오는 함수
def get_base_header() -> Dict[str, str]:
    if _auto_reauth:
        re_auth()
    return copy.deepcopy(_base_headers)


# 환경 설정값을 저장하는 함수
def set_tr_env(cfg: Dict[str, str]) -> None:
    global _TRENV
    _TRENV = _TRENV(
        my_app=cfg["my_app"],
        my_sec=cfg["my_sec"],
        my_acct=cfg["my_acct"],
        my_prod=cfg["my_prod"],
        my_token=cfg["my_token"],
        my_url=cfg["my_url"],
    )


def is_paper_trading() -> bool:
    return _is_paper


# 실전투자와 모의투자를 설정하는 함수
def change_tr_env(
    token_key: str, svr: str = "prod", product: str = _cfg["my_prod"]
) -> None:
    cfg = dict()

    global _is_paper
    if svr == "prod":
        ak1, ak2 = "my_app", "my_sec"
        _is_paper = False
    elif svr == "vps":
        ak1, ak2 = "paper_app", "paper_sec"
        _is_paper = True

    cfg["my_app"] = _cfg[ak1]
    cfg["my_sec"] = _cfg[ak2]

    if svr == "prod" and product == "01":
        cfg["my_acct"] = _cfg["my_acct_stock"]
    elif svr == "prod" and product == "30":
        cfg["my_acct"] = _cfg["my_acct_stock"]
    elif svr == "prod" and product == "03":
        cfg["my_acct"] = _cfg["my_acct_future"]
    elif svr == "prod" and product == "08":
        cfg["my_acct"] = _cfg["my_acct_future"]
    elif svr == "vps" and product == "01":
        cfg["my_acct"] = _cfg["my_paper_stock"]
    elif svr == "vps" and product == "03":
        cfg["my_acct"] = _cfg["my_paper_future"]

    cfg["my_prod"] = product
    cfg["my_token"] = token_key
    cfg["my_url"] = _cfg[svr]

    set_tr_env(cfg)


def get_result_object(json_data: Dict[str, Any]) -> namedtuple:
    result_object = namedtuple("res", json_data.keys())
    return result_object(**json_data)


# 토큰 발급 함수
def auth(svr: str = "prod", product: str = _cfg["my_prod"], url: str = None) -> None:
    p = {"grant_type": "client_credentials"}
    ak1, ak2 = ("my_app", "my_sec") if svr == "prod" else ("paper_app", "paper_sec")

    p["appkey"] = _cfg[ak1]
    p["appsecret"] = _cfg[ak2]

    saved_token = read_token()
    if saved_token is None:
        url = f"{_cfg[svr]}/oauth2/tokenP"
        res = requests.post(url, data=json.dumps(p), headers=get_base_header())
        rescode = res.status_code
        if rescode == 200:
            my_token = get_result_object(res.json()).access_token
            my_expired = get_result_object(res.json()).access_token_token_expired
            save_token(my_token, my_expired)
        else:
            print("Get Authentication token fail!\nYou have to restart your app!!!")
            return
    else:
        my_token = saved_token

    change_tr_env(f"Bearer {my_token}", svr, product)

    _base_headers["authorization"] = _TRENV.my_token
    _base_headers["appkey"] = _TRENV.my_app
    _base_headers["appsecret"] = _TRENV.my_sec

    global _last_auth_time
    _last_auth_time = datetime.now()

    if _debug:
        print(f"[{_last_auth_time}] => get AUTH Key completed!")


# 토큰 재발급 함수
def re_auth(svr: str = "prod", product: str = _cfg["my_prod"]) -> None:
    if (datetime.now() - _last_auth_time).seconds >= 86400:
        auth(svr, product)


def get_env() -> Dict[str, str]:
    return _cfg


def get_tr_env() -> namedtuple:
    return _TRENV


# 주문 API에서 사용할 hash key값을 발급받아 header에 설정해주는 함수
def set_order_hash_key(headers: Dict[str, str], params: Dict[str, Any]) -> None:
    url = f"{get_tr_env().my_url}/uapi/hashkey"

    res = requests.post(url, data=json.dumps(params), headers=headers)
    if res.status_code == 200:
        headers["hashkey"] = get_result_object(res.json()).HASH
    else:
        print("Error:", res.status_code)


# API 호출 응답에 필요한 처리 공통 함수
class APIResponse:
    def __init__(self, response: requests.Response):
        self._response_code = response.status_code
        self._response = response
        self._header = self._set_header()
        self._body = self._set_body()
        self._error_code = self._body.msg_cd
        self._error_message = self._body.msg1

    def _set_header(self) -> namedtuple:
        header_fields = {
            x: self._response.headers.get(x)
            for x in self._response.headers.keys()
            if x.islower()
        }
        return namedtuple("header", header_fields.keys())(**header_fields)

    def _set_body(self) -> namedtuple:
        return namedtuple("body", self._response.json().keys())(**self._response.json())

    def is_ok(self) -> bool:
        try:
            return self._body.rt_cd == "0"
        except:
            return False

    def print_error(self, url: str) -> None:
        print(
            "-------------------------------\nError in response: ",
            self._response_code,
            " url=",
            url,
        )
        print(
            "rt_cd : ",
            self._body.rt_cd,
            "/ msg_cd : ",
            self._error_code,
            "/ msg1 : ",
            self._error_message,
        )
        print("-------------------------------")


# API 호출 공통 함수
def url_fetch(
    api_url: str,
    transaction_id: str,
    transaction_cont: str,
    params: Dict[str, Any],
    append_headers: Dict[str, str] = None,
    post_flag: bool = False,
    hash_flag: bool = True,
) -> APIResponse:
    url = f"{get_tr_env().my_url}{api_url}"
    headers = get_base_header()

    if transaction_id[0] in ("T", "J", "C") and is_paper_trading():
        transaction_id = "V" + transaction_id[1:]

    headers["tr_id"] = transaction_id
    headers["custtype"] = "P"
    headers["tr_cont"] = transaction_cont

    if append_headers:
        headers.update(append_headers)

    if _debug:
        print("< Sending Info >")
        print(f"URL: {url}, TR: {transaction_id}")
        print(f"<header>\n{headers}")
        print(f"<body>\n{params}")

    if post_flag:
        res = requests.post(url, headers=headers, data=json.dumps(params))
    else:
        res = requests.get(url, headers=headers, params=params)

    if res.status_code == 200:
        return APIResponse(res)
    else:
        print("Error Code : " + str(res.status_code) + " | " + res.text)
        return None
