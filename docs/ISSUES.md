# Project Issues

1. When a student selects an invalid quiz number, the code that's supposed to catch this prints nothing — the value meant to be an error message just gets thrown away and the program moves on as if nothing happened ✅
2. The "have you already taken this quiz" check compares against the subject of whatever quiz happened to be printed last in the menu listing, not the one the student actually picked. ✅
3. The boundary check for valid quiz selection numbers is off by one — picking the very last valid number works, but the number directly after that should be rejected and isn't, leading to a crash instead. ✅
4. Typing "ADMIN" at the very first prompt grants full access to add, view, and delete every student and teacher record — no password required, unlike every other privileged action in the app ✅
5. Inside one function, a variable is named identically to a module that's imported at the top of the same file — currently harmless because the two never collide in execution order, but a future edit that calls the module after that variable is created will silently break ✅
6. After completing any single menu action (adding a student, viewing a list, anything), the program exits entirely — there's no way to perform a second action without restarting it from the terminal. ✅
7. Two of the three menu files import several functions that are never called anywhere in those files. ✅
8. A handwritten note in your own project documentation claims a specific save operation doesn't work — but testing the current data suggests it might already be fixed, or only fails under specific conditions you haven't pinned down--👀
9. Three different places ask the user to type a number and immediately convert it — typing literally anything else (a letter, a symbol, just pressing Enter) crashes the whole program on the spot. ✅
10. Every teacher's password is stored as plain readable text in a file that your version control is currently set up to track and upload — including to a public remote if you . 👀
11. A list comprehension reuses the same name as the list it's building from, even though each item represents something singular and different from what the original variable name implied — it works, but it's a trap for future-you trying to read this in three weeks. ✅
12. One of your four model classes is fully written with its own attributes but is never imported, instantiated, or referenced anywhere else in the project — it's pure dead weight right now.✅
13. Two of your classes have a counting mechanism (an attribute plus a method meant to increment it) that is never triggered anywhere — no matter how many objects you create, the counter stays at zero forever. ✅
14. Some of the quiz questions and answer options used as test data contain language you'd probably regret if a recruiter opened this repo. ✅
15. One section of your planning document was left as a header with nothing underneath it. ✅
16. The project has no README at all, despite that being a written requirement you set for yourself before starting. ✅
17. A file your code editor generates automatically for running scripts has been committed into the repo right alongside your actual source code.✅
