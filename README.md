# :lion:2021 멋쟁이사자처럼 해커톤 
 
## 1. 참여 과제

주제: 가치사자(같이 가치있게 사자!)
- 전국 대학생을 대상으로한 자취생 공동구매 플랫폼 제작 (Purchase-mate)

### 1.1 팀명 : 가치살래

### 1.2 팀 구성

본 해커톤 프로젝트에 참여하는 Purchase-mate 팀의 팀원은 다음과 같다. (가나다 순으로 나열)

- [김시윤](https://github.com/sharon1638)
- [박상준](https://github.com/tkdwns414) (팀장)
- [이태검](https://github.com/LeeTaeGeom)
- [이형석](https://github.com/lhs961021)
- [임도연](https://github.com/dddooo9)

## 2. 프로그래밍 언어

본 해커톤 프로젝트는 
[**Python**](https://www.python.org)을 메인 프로그래밍 언어를 사용하고,
[**Django**](https://www.djangoproject.com)을 메인으로 이용한다.

### 2.1. 버전 정보

본 해커톤 프로젝트는 
- Python 3.9.1 버전
- Django 3.1.6 버전
 
을 이용한다.

### 2.2. 외부 라이브러리

본 애플리케이션을 구현하는 과정에서 활용 가능한 외부 라이브러리는 제한없이 사용하는 것을 원칙으로 한다.

### 2.3. Requirements.txt

본 애플리케이션의 소스코드 내에서 활용한 모든 외부 라이브러리는 requirements.txt에 해당 라이브러리 리스트를 저장하여 팀원들에게 공유하여야 한다.
```
$ pip freeze > requirements.txt
```
requirements.txt에 저장된 외부 라이브러리를 다운로드 받는 명령어는 다음과 같다.
```
$ pip install -r requirements.txt
```
### 2.4. Python 가상환경

#### 2.4.1. 주요 가상환경 프로그램
- [pipenv](https://github.com/pypa/pipenv) :  Python.org에서 공식적으로 권장하는 패키지 설치 툴 및 가상환경 구현용 프로그램

## 3. 서버 실행
```
$ python manage.py runserver 
```
## 4. 환경변수 파일

.gitignore

- Git 관련 환경변수 파일

requirements.txt

- 파이썬 라이브러리 종속성 파일

## 5. 동국대 이메일로 로그인 하는 경우

https://wave1994.tistory.com/100 참고

## 6. 배포

서버 배포는 aws EC2의 Ubuntu Server 18.04 LTS (HVM), SSD Volume Type - 64bit, t2.micro(프리티어) 인스턴스를 이용한다. 
