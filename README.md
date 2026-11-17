# PYTHON FILE HANDLING, MODULES AND PACKAGES ASSIGNMENT

## Student Details

- **Student Name:** Ranjitha. R
- **Register Number:** 192421285
- **Course Outcome:** C04
- **Assignment Type:** Individual
- **Total Marks:** 50
- **Department:** Information Technology

---

## 1. Project Overview

This project is developed as part of the Python File Handling, Modules and Packages assignment.

The main objective is to design and implement Python programs using file handling, modules and packages to process and analyse data effectively.

This project covers reading and writing files, handling exceptions, validating records, organising programs into modules and packages, and generating reports.

## 2. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| VS Code | Code editor |
| Git | Version control |
| GitHub | Project hosting and submission |
| Text Files (.txt) | Input data storage |
| CSV Files (.csv) | Structured output reports |

## 3. Software Requirements

- Python 3.12 or later
- Visual Studio Code
- Git
- GitHub account

### Libraries Used

The project uses Python standard libraries:

- pathlib – File and directory management
- csv – CSV file processing
- os – Operating system operations
- sys – Command-line arguments
- tempfile – Temporary file creation
- re – Email format validation

No external Python packages are required.

## 4. Project Structure

```text
Python_File_Handling_Assignment/
│
├── README.md
├── requirements.txt
├── Assignment_Report.docx
│
├── Task01/
│   ├── solution.py
│   ├── mess_oct.txt
│   ├── mess_report.txt
│   └── pseudocode.txt
│
├── Task02/
│   ├── attendance_month.py
│   ├── daily_files/
│   ├── output/
│   └── pseudocode.txt
│
├── Task03/
│   ├── attendance_processor.py
│   └── pseudocode.txt
│
├── Task04/
│   ├── solution.py
│   ├── day1.txt
│   ├── day2.txt
│   ├── day3.txt
│   ├── returns.log
│   └── pseudocode.txt
│
├── Task05/
│   ├── organisation_a/
│   ├── organisation_b/
│   ├── organisation_c/
│   ├── organisation_d/
│   ├── README.md
│   └── pseudocode.txt
│
└── Task06/
    ├── main.py
    ├── data/
    ├── output/
    ├── festdesk/
    │   ├── __init__.py
    │   ├── reader.py
    │   ├── validator.py
    │   └── processor.py
    └── pseudocode.txt
```

## 5. Task Descriptions

### Task 1: File-Processing Design Review – Diagnose and Repair a Poor Script (6 Marks)

This task identifies the problems in a hostel mess-bill processing program and provides a corrected solution.

**Key concepts:**
- File handling using the `with` statement.
- Reading files line by line.
- Handling decimal values.
- Exception handling.
- Recording rejected records.
- Calculating the total bill amount.

**Output:** Mess bill report containing accepted records, total amount and rejected records.

### Task 2: Biometric Attendance File Processing (8 Marks)

This task processes daily biometric attendance files and generates monthly attendance reports.

**Key concepts:**
- Reading multiple daily files.
- Dictionary-based data storage.
- Counting present and absent days.
- Calculating attendance percentages.
- Identifying students below 75% attendance.
- Logging damaged records.

**Output files:**
- attendance_percentage.csv
- below_75_percent.csv
- damaged_lines.log

### Task 3: Exception Handling in the Attendance Processor (9 Marks)

This task demonstrates exception handling in an attendance processing system.

**Key concepts:**
- FileNotFoundError
- PermissionError
- UnicodeDecodeError
- ValueError
- IndexError
- Custom exception using InvalidRecord.
- try, except and finally statements.
- Exception propagation.

**Output:** Attendance summary with invalid records and error details.

### Task 4: File and Exception Forensics (7 Marks)

This task identifies and repairs defects in a library returned-books logging program.

**Key concepts:**
- File opening modes.
- Write mode and append mode.
- Newline handling.
- Context managers.
- File closing and exception safety.

**Output:** A complete returned-books log containing records from all three days.

### Task 5: The Same Utility Organised Four Ways (7 Marks)

This task implements the same attendance utility using four different program structures.

**Four organisations:**

1. One Python script.
2. One module imported by a main script.
3. Three modules in one folder.
4. A Python package with `__init__.py` and submodules.

**Key concepts:**
- Functions and modules.
- Import statements.
- Package creation.
- Code reusability.
- Maintainability and testing.

### Task 6: Design Challenge – College Fest Registration Desk (13 Marks)

This task develops a college fest registration processing system using Python packages.

The system processes registration files from five departments.

**Key concepts:**
- Reading multiple department files.
- Validating registration details.
- Email validation.
- Detecting duplicate register numbers.
- Handling damaged records.
- Generating event-wise participant lists.
- Generating summary reports.
- Error logging.

**Output files:**
- master_list.csv
- Event-wise participant CSV files.
- summary.txt
- errors.log

## 6. How to Execute the Programs

### Step 1: Install Python

Check whether Python is installed:

```bash
python --version
```

### Step 2: Open the Project

Open the extracted project folder in Visual Studio Code.

### Step 3: Open the Terminal

Select Terminal → New Terminal.

### Step 4: Execute the Programs

Run the following commands from the main project directory.

**Task 1**

```bash
python Task01/solution.py
```

**Task 2**

```bash
python Task02/attendance_month.py
```

**Task 3**

```bash
python Task03/attendance_processor.py
```

**Task 4**

```bash
python Task04/solution.py
```

**Task 5**

```bash
python Task05/organisation_a/main.py
python Task05/organisation_b/main.py
python Task05/organisation_c/main.py
python Task05/organisation_d/main.py
```

**Task 6**

```bash
python Task06/main.py
```

## 7. Testing and Validation

The programs are designed to handle the following test conditions:

- Valid input records.
- Missing input files.
- Empty files.
- Incorrect field counts.
- Invalid numerical values.
- Invalid attendance status.
- Damaged records.
- Duplicate registrations.
- Invalid email addresses.
- Permission and encoding errors.

Each program produces the appropriate output or records the error information.

## 8. Time and Space Complexity

The assignment analyses alternative approaches and their complexity.

| Task | Main Approach | Time Complexity |
|---|---|---|
| Task 1 | Line-by-line file processing | O(n) |
| Task 2 | Dictionary-based attendance counting | O(L) expected |
| Task 3 | Line-by-line validation | O(n) |
| Task 4 | Append-based log processing | O(n) |
| Task 5 | Modular function organisation | Depends on input size |
| Task 6 | Dictionary-based duplicate detection | O(N) expected |

Here, n represents the number of input characters or records as applicable, L represents total attendance lines, and N represents registration records.

## 9. Expected Learning Outcomes

After completing this assignment, the following concepts are demonstrated:

1. Understanding Python file handling.
2. Reading and writing text and CSV files.
3. Implementing exception handling.
4. Creating and using custom exceptions.
5. Processing large files efficiently.
6. Organising Python programs into modules.
7. Creating reusable Python packages.
8. Validating input data and handling errors.
9. Analysing time and space complexity.
10. Using Git and GitHub for project submission.

## 10. Conclusion

This assignment provides practical experience in Python file handling, exception handling, modules and packages.

All six tasks demonstrate how Python can be used to process real-world data, identify errors, validate records and generate meaningful reports.

The project also demonstrates the importance of writing reliable, reusable, maintainable and efficient programs.
