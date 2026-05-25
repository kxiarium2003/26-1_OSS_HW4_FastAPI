# OSS HW4 - FastAPI

2026학년도 1학기 오픈소스소프트웨어실습 HW4 과제입니다.

FastAPI를 이용하여 수강기록(Course Records)을 관리하는 간단한 REST API 서버를 구현하였습니다.

---

## 구현 기능

### GET /courses

- 현재 저장된 전체 수강기록을 반환합니다.
- JSON 파일(`courses.json`)의 데이터를 읽어와 반환합니다.

### POST /courses

- 새로운 수강기록을 추가합니다.
- 전달받은 JSON 데이터를 기존 리스트에 추가한 뒤 다시 파일에 저장합니다.

---

## 프로젝트 구조

```text
26-1_OSS_HW4_FastAPI/
├── main.py
├── courses.json
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 실행 방법

#### 1. 가상환경 생성

```bash
python3 -m venv venv
```

#### 2. 가상환경 활성화

```bash
source venv/bin/activate
```

#### 3. 패키지 설치

```bash
pip install -r requirements.txt
```

#### 4. FastAPI 서버 실행

```bash
uvicorn main:app --reload
```

---

## 서버 주소

```text
http://127.0.0.1:8000
```

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

---

## 예시 요청

#### GET /courses

```text
GET http://127.0.0.1:8000/courses
```

#### POST /courses

```text
POST http://127.0.0.1:8000/courses
```

Request Body:

```json
{
  "course_name": "오픈소스소프트웨어실습",
  "year": "2026",
  "semester": "1",
  "grade": "A+"
}
```

---

### 개발 환경

- Python 3
- FastAPI
- Uvicorn
- VS Code
- Postman