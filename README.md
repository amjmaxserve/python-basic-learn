# 🐍 Python From Scratch — Learning Journey

A progressive, hands-on collection of Python scripts covering core fundamentals — built step by step, from variables to real-world mini-projects.

---

## 📖 About This Repository

This repository documents a personal journey of learning Python from the ground up. Each numbered file builds on the previous one, introducing new concepts and gradually increasing in complexity. The central theme throughout the exercises is a **Days-to-Units Converter** — a simple program that evolves from a static script into a modular, well-structured application as new Python concepts are introduced.

---

## 🗂️ File Overview

| # | File | Topic | Description |
|---|------|--------|-------------|
| 01 | `01-main.py` | Variables & f-strings | Declares variables and uses f-strings to print day-to-second conversions |
| 02 | `02-function.py` | Functions | Extracts conversion logic into a reusable `days_to_units()` function |
| 03 | `03-user-inputs.py` | User Input | Accepts dynamic user input and converts it using the function |
| 04 | `04-if-condition.py` | Conditionals & Data Types | Adds `if/else` validation and explores Python's core data types |
| 05 | `05-error-handling.py` | Error Handling | Wraps logic in `try/except` to gracefully handle invalid inputs |
| 06 | `06-user-exit.py` | While Loops | Keeps the program running in a loop until the user types `exit` |
| 07 | `07-for-loops.py` | For Loops | Accepts comma-separated input and processes each value with a `for` loop |
| 08 | `08-lists.py` | Lists | Introduces Python lists: indexing, `append()`, and iteration |
| 09 | `09-comments.py` | Comments & Docstrings | Demonstrates single-line comments (`#`) and multi-line docstrings (`"""`) |
| 10 | `10-set.py` | Sets | Uses Python `set` to eliminate duplicate values from user input |
| 11 | `11-set-1.py` | Sets (standalone) | A minimal standalone example of creating and iterating over a set |
| 12 | `12-dictionary.py` | Dictionaries & All Data Types | Uses a dictionary to structure input; showcases all Python data types |
| 13 | `13-modules.py` | Custom Modules | Imports and uses functions from a custom helper module |
| 13 | `13-helper-module.py` | Helper Module | Defines reusable functions (`days_to_units`, `validate_and_execute`) as a module |
| 14 | `14-builtin-modules.py` | Built-in Modules | Explores `math`, `datetime`, `os`, and `logging` standard library modules |
| 15 | `15-time-till-deadline.py` | Mini Project | Calculates the time remaining until a user-defined goal deadline in days and hours |

---

## 🧠 Concepts Covered

### 🔤 Core Syntax
- Variables and assignment
- f-strings (formatted string literals)
- Data types: `str`, `int`, `float`, `bool`, `complex`

### ⚙️ Functions
- Defining and calling functions with `def`
- Parameters and return values
- Scope (local vs. global variables)

### 🧭 Control Flow
- `if`, `elif`, `else` conditionals
- `while` loops with an exit condition
- `for` loops over lists and sets

### 🛡️ Error Handling
- `try` / `except` blocks
- Handling `ValueError` for invalid user input

### 📦 Data Structures
- **Lists** — ordered, mutable, allows duplicates (`[]`)
- **Sets** — unordered, no duplicates (`{}`)
- **Dictionaries** — key-value pairs (`{"key": "value"}`)

### 🧩 Modules
- **Custom modules** — splitting code into separate `.py` files and importing with `from module import function`
- Import styles: `import x`, `from x import y`, `import x as alias`, `from x import *`
- **Built-in standard library modules**:
  - `math` — `pow()`, `sqrt()`, `floor()`, `ceil()`
  - `datetime` — `datetime.now()`, `strptime()`, `timedelta`
  - `os` — operating system interface
  - `logging` — application-level logging with `getLogger()`

### 📝 Code Quality
- Single-line comments with `#`
- Multi-line docstrings with `"""`
- Inline documentation for functions and blocks

---

## 🚀 Running the Scripts

Make sure you have Python 3 installed:

```bash
python3 --version
```

Run any script directly from the project directory:

```bash
python3 01-main.py
python3 15-time-till-deadline.py
```

> **Note:** Scripts from `03` onwards require user input. Follow the on-screen prompts.
> For `06` and `07`, type `exit` to quit the running loop.

---

## 🌟 Mini Project — Time Till Deadline (`15-time-till-deadline.py`)

The final script is a practical mini-project that ties together **user input**, **`datetime` module**, **string parsing**, and **arithmetic** to compute how much time remains until a personal goal deadline.

**Usage:**
```
Enter your goal with a deadline separated by colon
Learn Python:31.12.2026
```

**Output:**
```
Dear user!, time remaining for your goal: Learn Python is 230 days
Dear user!, time remaining for your goal: Learn Python, is 5520 Hours
```

**Input format:** `<goal>:<DD.MM.YYYY>`

---

## 📚 Learning Path

```
Variables & f-strings
        ↓
    Functions
        ↓
  User Input
        ↓
  Conditionals
        ↓
 Error Handling
        ↓
  While Loops
        ↓
   For Loops
        ↓
     Lists
        ↓
   Comments
        ↓
     Sets
        ↓
 Dictionaries
        ↓
Custom Modules
        ↓
Built-in Modules
        ↓
  Mini Project 🎉
```

---

## 🛠️ Requirements

- **Python 3.x** (no third-party packages required)
- All modules used (`math`, `datetime`, `os`, `logging`) are part of the Python standard library

---

## 💡 Key Takeaways

> Python's power lies in its readability and its rich standard library. By building the same program incrementally — adding error handling, loops, data structures, and modules — you see exactly *why* each concept exists and *how* it improves your code.

## real Project 

> checkout the branch to project from this repository and you will find a realtime Project on Inventory management and analysis using openpyxl and basic python.

---

*Happy coding! 🚀*
