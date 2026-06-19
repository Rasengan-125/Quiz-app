# Quiz App

A command-line quiz application that lets teachers set quizzes and students take them. Built entirely in Python with JSON-based persistent storage.

---

## What Does It Do?

Starts by asking if you are a **teacher** or **student**.

- **Teacher flow:** authenticate with staff password → create quizzes, view scores, search students, rank by average grade
- **Student flow:** enter matric number → select a course → take a timed quiz → view your score

---

## Project Structure

```
Quiz_App--Python/
│
├── main.py                      # Entry point
├── models.py                    # Quiz, Student, Teacher classes
├── menus/
│   ├── admin.py                 # Admin menu logic
│   ├── teacher.py               # Teacher menu logic
│   └── student.py               # Student menu logic
├── services/
│   ├── quiz_service.py          # Quiz creation and quiz-taking logic
│   ├── student_service.py       # Student management
│   ├── teacher_service.py       # Teacher management
│   └── helpers.py               # Score management, auth, utilities
├── data/
│   ├── teachers.json            # Teacher records
│   ├── quizzes.json             # Quiz data
│   ├── students.json            # Student records and scores
│   └── grades.json              # Grade history
└── README.md
```

---

## Classes

### `Quiz`

| Field          | Type   | Description                     |
| -------------- | ------ | ------------------------------- |
| `subject`      | `str`  | Course code e.g. `MTH202`       |
| `teacher_name` | `str`  | Name of the teacher who set it  |
| `time`         | `int`  | Duration of the quiz in seconds |
| `questions`    | `list` | List of question dicts          |

Each question:

```json
{
  "question": "What is 2 + 2?",
  "options": ["A. 3", "B. 4", "C. 5", "D. 6"],
  "answer": "B"
}
```

### `Student`

| Field     | Type    | Description                       |
| --------- | ------- | --------------------------------- |
| `name`    | `str`   | Student's full name               |
| `matric`  | `str`   | Matric number                     |
| `scores`  | `dict`  | Subject → score mapping           |
| `average` | `float` | Average score across all subjects |
| `status`  | `str`   | `Active` or `Inactive`            |

### `Teacher`

| Field      | Type  | Description                           |
| ---------- | ----- | ------------------------------------- |
| `name`     | `str` | Teacher's full name                   |
| `email`    | `str` | Staff email address                   |
| `password` | `str` | Hashed password (plain text in dev)   |
| `status`   | `str` | `Active` or `Inactive`                |
| `hired`    | `str` | Date hired                            |
| `resign`   | `str` | Date resigned (empty if still active) |

---

## Data Files

| File            | Format | Contains                                                        |
| --------------- | ------ | --------------------------------------------------------------- |
| `teachers.json` | JSON   | Teacher name, email, password, status                           |
| `quizzes.json`  | JSON   | Quiz subject, teacher, questions and answers                    |
| `students.json` | JSON   | Student name, matric, scores, average                           |
| `grades.json`   | JSON   | History log of every quiz attempt (not used as source of truth) |

---

## User Flow

### Teacher

1. Select **Teacher** at login
2. Authenticate with staff email and password (3 attempts max)
3. Choose from menu:
   - Create a new quiz
   - View all students and scores
   - Search student by matric number
   - Rank students by average grade

### Student

1. Select **Student** at login
2. Enter matric number
3. Select a course from the available quizzes
4. Answer questions one by one within the time limit
5. View score at the end

---

## Edge Cases Handled

- Wrong password — 3 attempts then access denied
- Invalid matric number — denied with message
- Student takes a quiz they already completed — blocked
- Empty or invalid input on number fields — re-prompts with error
- JSON file empty or missing — returns empty list safely
- Student has no scores yet — average defaults to `0`
- Quiz timer runs out mid-question — quiz ends immediately

---

## Password Strategy

Passwords are stored as plain text during development for simplicity. Before deployment, all passwords will be hashed using `bcrypt` — each password will be salted and hashed on registration, and verified using `bcrypt.checkpw()` on login. No plain text passwords will exist in production.

---

## Requirements

```bash
pip install bcrypt
```

No other third-party dependencies. Built with Python 3.7+ standard library.

---

## Running the App

```bash
python main.py
```

Always run from the project root, never from inside a subfolder.

## Known Limitations

- The timer is checked between questions, not during input — a student
  who pauses mid-question and answers after time technically expires
  will still have that answer counted.
