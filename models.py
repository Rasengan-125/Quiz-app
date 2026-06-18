from datetime import datetime


class Teacher:
    def __init__(
        self,
        name,
        email,
        password,
        status="Active",
        hired=datetime.now().strftime("%d %B %Y, %I:%M %p"),
        resign="",
    ):
        self.name = name
        self.email = email
        self.password = password
        self.status = status
        self.hired = hired
        self.resign = resign

    def __str__(self):
        return f"{self.name}"


class Student:
    count = 0

    def __init__(self, name, matric, scores=None, status="Active"):
        self.name = name
        self.matric = matric
        self.scores = scores if scores is not None else {}
        self.status = status

    @classmethod
    def counts(cls):
        Student.count += 1

    def __str__(self):
        return f"{self.name} | Matric: {self.matric}"


class Quiz:
    count = 0

    def __init__(self, subject, teacher_name, time, questions=None):
        self.subject = subject
        self.teacher_name = teacher_name
        self.time = time
        self.questions = questions if questions is not None else []

    @classmethod
    def counts(cls):
        Quiz.count += 1

    def __str__(self):
        return f"{self.subject} — set by {self.teacher_name}"


class Grade:
    def __init__(self, matric, grades=None):
        self.matric = matric
        self.grades = grades if grades is not None else {}
