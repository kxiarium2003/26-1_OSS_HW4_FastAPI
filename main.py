from fastapi import FastAPI
from pydantic import BaseModel
import json

app = FastAPI()

JSON_FILE = "courses.json"


class Course(BaseModel):
    course_name: str
    year: str
    semester: str
    grade: str


def load_courses():
    with open(JSON_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_courses(data):
    with open(JSON_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


@app.get("/courses")
def get_courses():
    data = load_courses()
    return data


@app.post("/courses")
def add_course(course: Course):
    data = load_courses()

    new_course = {
        "course_name": course.course_name,
        "year": course.year,
        "semester": course.semester,
        "grade": course.grade
    }

    data.append(new_course)

    save_courses(data)

    return {
        "message": "Course added successfully",
        "added_course": new_course
    }