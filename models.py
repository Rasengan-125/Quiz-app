class Teacher:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def __str__(self):
        return f"{self.name}"


class Student:
    count = 0

    def __init__(self, name, matric, scores=None):
        self.name = name
        self.matric = matric
        self.scores = scores if scores is not None else {}

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
