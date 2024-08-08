# job-a-dream-backend

This template should help get you started developing with Python.

## 요구 사항

- Python 3.12 (tested under Python 3.12.4)

## 설정

해당 Repository는 Python 3.12와 `.venv` 가상환경을 사용합니다. 아래 단계에 따라 가상환경을 설정하고 의존성을 설치하세요.

### 1. Python 3.12 설치

Python 3.12가 시스템에 설치되어 있는지 확인하세요. 설치되어 있지 않다면 [Python 공식 웹사이트](https://www.python.org/downloads/)에서 다운로드하고 설치하세요.

### 2. 가상환경 생성

프로젝트 디렉토리에서 아래 명령어를 실행하여 `.venv`라는 이름의 가상환경을 생성합니다:

```bash
python -3.12 -m venv .venv
```

### 3. 가상환경 활성화

Windows:

```bash
.venv\Scripts\activate
```

macOS 및 Linux:

```bash
source .venv/bin/activate
```

### 4. 의존성 설치

가상환경이 활성화된 상태에서, requirements.txt 파일에 명시된 의존성을 설치합니다:

```bash
pip install -r requirements.txt
```

### 5. 실행

```bash
python main.py
```
