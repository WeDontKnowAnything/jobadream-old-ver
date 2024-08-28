# 🦉jobAdream
구직자의 관점으로 바라보는 취업 플랫폼   

<img src="https://github.com/user-attachments/assets/0e978d37-d822-439b-90c3-186b623f49b7" width="400" height="400"/>

## 👥 팀원 소개

![image](https://github.com/user-attachments/assets/6ccbaa49-516b-40fd-87c7-89067eb20b5d)
| 박중헌 (PM) | 문희선 | 오승민 | 송영빈 |
|:----------:|:----------:|:----------:|:----------:|
| 프로젝트 총괄/기획<br>팀 관리 및 조정<br>프론트엔드 개발<br>깃 관리|데이터베이스/ERD 설계<br>데이터 전처리/분석<br>백엔드 개발<br>회의 문서 작성|아키텍처 설계<br>데이터 전처리/분석<br>백엔드 개발|프론트엔드 설계<br>데이터 전처리|
| [@qjrm1430](https://github.com/qjrm1430) | [@MoonHeesun](https://github.com/MoonHeesun) | [@artemIntellectus](https://github.com/artemIntellectus) | [@GETSPRING8230](https://github.com/GETSPRING8230) |




## 1. 프로젝트 개요
최근 금융 위기와 글로벌화 기술 발전 산업 구조 변화 등으로 인해 중소기업과 스타트업의 경영 환경이 급격히 변화하고 있다. 이러한 상황에서 기업의 휴폐업을 정확하게 예측하는 모델의 필요성이 증가하고 있다. 본 프로젝트는 대기업, 중견기업, 강소기업 뿐 아니라 비재무 데이터를 활용한 중소기업 및 스타트업의 휴폐업을 예측하는 모델을 개발하여, 이를 기반으로 구직자가 신뢰성 있는 기업 평가 정보를 제공받을 수 있는 구인구직 사이트를 구축하고자 한다.   

### 📌 프로젝트 목표
- 구직자가 지원하려는 기업에 대한 종합적인 평가를 제공하여 정보 불균형을 해소
- 재무 및 비재무 데이터를 통합하여 유동적인 환경에 맞춘 객관적이고 신뢰성 있는 정보를 제공
- 구직자가 신뢰성 있는 기업 평가 정보를 제공받을 수 있도록 지원


### 📌 프로젝트 주요 기능
- 기업 평가 데이터 제공
- 해당 기업에 대한 채용공고 플랫폼 링크 조회 시각화
- 기업 조회 검색 및 필터 기능

## 2. 아키텍처 설계
![JOBADREAM drawio](https://github.com/user-attachments/assets/bffa0e80-22ac-4bcb-aa43-f1bf6c51bf46)

## 3. Database 설계
![image](https://github.com/user-attachments/assets/c0ec4088-eddb-4f6a-bdc9-bdc31e52a0eb)

## 4. UI 설계
![image](https://github.com/user-attachments/assets/aacbaa45-4db8-4837-8d6e-f0a602f43199)

## 5. 개발환경
- Server : Docker, Ubuntu, Nginx
- AWS : Relationship Database Service, S3, CloudFront, Route53, Elastic Container Registry, Elastic Container Service, Code Pipeline, Code Build, Code Deploy, Elastic Load Balancing, Certificate Manager, Lambda
(이하 : RDS, S3, CloudFront, Route53, ECR, ECS, Code Pipeline, Code Build, Code Deploy, ELB, CM, Lambda)
- 프레임워크 : Vue.js, FastAPI, Spark
- 사용 언어 : Python, Javascript
- 데이터베이스 : PostgreSQL
- ETC : Swagger, VSCode, Git/Github

## 1차 에자일 진행상황
- Database 구축
- 프론트엔드 홈, 기업, 채용정보, 게시판 페이지
- 도메인 등록 

