# Quiz App — Project Plan

---

## What Does It Do?

A CLI app that lets teachers set quizzes and students take quizzes.

- Starts by asking if you are a **teacher** or **student**
- **Teacher flow:** enter staff password → set quiz, view student scores, search student by name, rank students by average grade
- **Student flow:** enter matric number → select course → take quiz

---

## Classes

### Quiz Class

- `subject` — the course name
- `teacher_name` — name of the teacher who set it
- `questions` — list of question dicts

Each question:

```json
{
  "question": "What is 2 + 2?",
  "options": ["A. 3", "B. 4", "C. 5", "D. 6"],
  "answer": "B"
}
```

### Student Class

- `name` — student's full name
- `matric` — matric number
- `scores` — dict of subject → score

### Teacher Class

- `name` — teacher's full name
- `password` — hashed or plain password

---

## Files

| File            | Format | Contains                                          |
| --------------- | ------ | ------------------------------------------------- |
| `teachers.json` | JSON   | Teacher name and password                         |
| `quizzes.json`  | JSON   | Quiz subject, teacher name, questions and answers |
| `students.json` | JSON   | Student name, matric number, scores               |
| `scores.json`   | JSON   | Score history per student per subject             |

---

## User Flow

### Teacher

1. Select "Teacher" at login
2. Enter staff password
3. Choose from menu:
   - Set a new quiz
   - View students who took a quiz and their scores
   - Search student by name and view average grade
   - Rank students by average grade

### Student

1. Select "Student" at login
2. Enter matric number
3. Select course to take quiz on
4. Answer questions one by one
5. View score at the end

---

## Edge Cases to Handle

- Wrong password — deny access
- Invalid matric number — deny access
- Student takes a quiz they already completed — block or allow retake
- Empty input on any field
- Quiz file not found
- Student has no scores yet

---

## Password Strategy

Passwords are stored as plain text during development for simplicity. Before deployment, all passwords will be hashed using `bcrypt` — each password will be salted and hashed on registration, and verified using `bcrypt.checkpw()` on login. No plain text passwords will exist in production.
