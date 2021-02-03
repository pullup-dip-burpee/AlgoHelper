# AlgoHelper

알고리즘 공부를 도와주는 웹사이트(웹개발 연습용 플젝)

## 작업의 순서?
1. API 정리 - GitHub Wiki 사용
1. 요구사항 정리. 기능 무엇. 

- Backend
  - DB ERD 그리기
  - 가상환경 설치
  - requirements.txt 의 패키지들 설치
    - 미니콘다/아나콘다 설치된 후 `conda create -n algohelper python=3.8` 로 가상환경 만들기(최초 1회만)
    - `conda activate algohelper` 로 가상환경 실행
    - AlgoHelper 디렉토리로 진입 후 `pip install -r requirements.txt`로 패키지 설치
  - django 프로젝트 생성(여기서부턴 은천만)
    - `django-admin startproject algohelper`
    - app 만들기
  - API User, Posting, Reply 구현

- Frontend
  - 컨셉 잡기 - UI 틀 잡기. 폰트, 컬러, 창, 버튼 등 통일
  - Mock up 그리기(프로토타이핑)
  - 

- Deploy
  - AWS 계정 설정
  - AWS ec2, rds
  - 보안 그룹 설정
