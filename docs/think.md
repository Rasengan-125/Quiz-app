- Student enters matric number
- List of available quiz subject shows up
- Student picks a quiz by number
- The quiz is selected by using that number as an index of quizzes
- "Are you ready" message pops up. Enter to continue
- Timer starts
- The questions show up one by with options, and input to put answer, and the answers are kept in an array
- At the end, it compares each item in the answer array to the answer of the questions
- It computes the percentage of the score and stores it in the scores.json

## Saving to grades.json

- First, load all the grades into memory
- Find the grade in the list of grades with a matching matric number as the inputed one. If it doesn't exist, create a new grade
- If the matric number exists, check if the subject has been recorded already. Y? Overwrite it. N? Add subject, and it's score

## Problems.

- add_quiz won't add a new quiz to the quizzes.json. Correct that
