# CLI-Based Programming Assessment Platform

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Commands](#commands)
   - [SET_ENV](#set_env)
   - [CREATEUSER](#createuser)
   - [SETQUESTION](#setquestion)
   - [MAKE_DIR](#make_dir)
   - [EVALUATE](#evaluate)
   - [SUBMIT](#submit)
4. [Directory Structure](#directory-structure)
   - [Admin home Directory](#admin-home-directory)
   - [Program Lab Directory](#program-lab-directory)
   - [User's Home Directory](#users-home-directory)
5. [Usage](#usage)
   - [Setup Environment](#setup-environment)
   - [Create Users](#create-users)
   - [Make Directories](#make-directories)
   - [Set Questions](#set-questions) 
   - [Evaluate Submissions](#evaluate-submissions)
6. [Example Workflow](#example-workflow)
7. [Contributing](#contributing)
8. [License](#license)

## Introduction
This project is a CLI-based programming assessment platform designed to streamline the process of setting up and evaluating programming assignments. The platform leverages Linux user management and directory structures to isolate user environments and manage assessment scripts.

## Features
- **User Management:**
   - **CREATEUSER Command:** Automatically create Linux user accounts from a predefined list in userlist.txt. Each user will have a dedicated home directory for their programming assignments.
- **Environment Setup:**
   - **SET_ENV Command:** Initialize the environment by copying questions, private test cases, public test cases, and executables to the appropriate directories: `/java_lab/Questions/`, `/java_lab/private_test_case/`, `/java_lab/public_test_case/`, and `/java_lab/executables/`.
   - **MAKE_DIR Command:** Create a Programs directory in the home directory of each user, along with `Python` and `Java` subdirectories for organizing assignments.
- **Question Management:**
    - **SETQUESTION Command:** Distribute a specified question file to the `Java` and `Python` folders inside the `Programs` directory of every user, ensuring all users have access to the same assignment.

- **Assessment:**
   - **EVALUATE Command:** Run public test cases on a user's submission to provide immediate feedback.
   - **SUBMIT Command:** Run private test cases on a user's submission for final evaluation, ensuring comprehensive assessment coverage.
- **Isolation and Organization:**
  - Each user has a separate environment, preventing interference between users' work.
  - Clear directory structure for questions, test cases, and executables, simplifying management and grading.

These features combine to create a robust and efficient platform for managing and assessing programming assignments in a controlled, scalable manner.


## Commands

### SET_ENV

Before Executing `Set_Env` Command. Admin (or) Host Should Create the Directory in root folder (/) as this [Directory Structure](#program-lab-directory).<br>
Also Ensure that the Environment Directory is Created. Since  the Admin have to Create Directory in the program name it should be as same as the program file name and the Directory should consist of these files:

- `program_name.py` is the program that the host writes to check for the given inputs.
- `program_name.pub` is the public test case file designed for the respective program.
- `program_name.pri` is the private test case file designed for the respective program.(In both the private and public test case files the input should be splited  by '-----')
- `program_name.Q` is the file which contains the question of the Program.

The Command `Set_Env` Sets up the environment by copying questions, private test cases, public test cases, and executables to the respective directories:
- `/java_lab/Questions/`
- `/java_lab/private_test_case/`
- `/java_lab/public_test_case/`
- `/java_lab/executables/`


### CREATEUSER
Creates users from the `userlist.txt` file. Each user will have their own home directory.

### SETQUESTION
Copies the specified question file to the Java and Python folders within the `Programs` directory located in the home directory of each user.

### MAKE_DIR
Creates a `Programs` directory in the home directory of each user and sets up `Python` and `Java` directories as subdirectories.

### EVALUATE
Evaluates the Public Test Case for the Given Programming Questions and Shows the Actual Output and Expected Output and Shows the Result in the Tabular Format. If the program causes any error it shows that 'ERROR OCCURED' in the result. If the program exceeds the given time limit, it
shows that the time limit exceeded.

Result consist the information of the number of test cases and the count of passed test cases and failed test cases in Tabular format 

### SUBMIT
Evaluate the Private Test Case for the Given Programming Questions and Shows the Submission Report in the Tabular format. Submission Report Consist of the total number of test cases and the count of passed and failed test cases.
and the Runtime of the program. If the program causes any error, it displays the message 'ERROR OCCURED' in Submission Report.

`SUBMIT` command logs the submission information in the log file located in `/var/log/program_labs`. Log file consist of the information about the username, time, programming language used, program name, passed test case count, failed test case count, runtime. Log file stores these information in CSV (Comma Seperated Value) Format. <br><br>
Note :- `EVALUATE` and `SUBMIT` Command should be copied or moved to `/usr/bin/`. Since it should be accessable to every user.

## Directory Structure
### Admin home Directory
/home/user<br>
├── project/ <br>
│ ├── Createuser<br>
│ └── MakeDir<br>
│ └── SetEnv<br>
│ └── SetQuestion<br>
│ └── Environment/ 


### Program Lab Directory
/program_lab/<br>
├── Questions/<br>
├── private_test_case/<br>
├── public_test_case/<br>
└── executables/


### User's Home Directory
/home/user<br>
├── Programs/ <br>
│ ├── Java/<br>
│ └── Python/<br>


## Usage
To use the CLI-Based Programming Assessment Platform, follow these steps:

### Setup Environment
Initialize the environment by setting up the required directories and copying necessary files.
```shell
./SET_ENV <program_name>
```
Replace <program_name> with the path to your program name.

### Create Users
Create user accounts based on the usernames listed in userlist.txt.
```shell
./CREATEUSER
```

### Make Directories
Create the Programs directory in the home directory of each user, along with Java and Python subdirectories.
```shell
./MAKE_DIR
```

### Set Questions
Distribute the specified question file to the Java and Python folders within the Programs directory located in the home directory of each user.
```shell
./SETQUESTION <question_file>
```
Replace <question_file> with the path to your question file.

### Evaluate Submissions
Evaluate Public Test Cases
Run public test cases and private test case for a given program with user's submission and Display its result with the Actual and Expected Output.
```shell
EVALUATE <program_name>
```

```shell
SUBMIT <program_name>
```
Note:- `EVALUATE` and `SUBMIT` Commands can be accessed by any user.

## Example Workflow
Consider that Factorial Program for the example.
### Admin Workflow
1. Makesure that the username are in the  `userlist.txt`.
```shell
./CREATEUSER
```

#### Setup Files
The given below files are stored inside Environment Directory.
       
1. Python file created by host named as `fact.py`.
```python
n = int(input())
fact = 1

for i in range(1, n + 1):
        fact *= i
print(fact)
```
2. Public Test case file created for factorial program and named as `fact.pub`.
```text
3
-----------
4
-----------
5
-----------
```
3. Private Test case file created for factorial program and named as `fact.pri`.
```text
1
---------
0
---------
7
---------
```
4. Question file created for factorial program and named as `fact.Q`.
```text
Find the Factorial for the given number.
```
2. After Setting up the required files. you can execute the `SET_ENV` command.
```shell
./SET_ENV fact
```
3. Create the Program file and the Question should be Commented in the file.
```shell
./SETQUESTION fact
```
Sample working example for [Admin workflow](https://drive.google.com/file/d/1F2G9yRPHwA90vt0W5fPIENwp1sIso6mx/view?usp=sharing)  
### User Workflow
After writing the program for the given question.
```shell
EVALUALTE fact
```
`EVALUATE` command is used to evalute public test case. it also shows the error with error message if any occurs.
The output format is: ![Evaluate Example](https://github.com/Karthi-J7/CLI-Based-Programming-Assessment-Platform/blob/main/assets/eval.png)
```shell
SUBMIT fact
```
`SUBMIT` command is used to evalute private test case and log the submission information. it ERROR_OCCURED if any error occurs.
The output format is:<img src="assets\submit.png">

Sample working example for [User workflow](https://drive.google.com/file/d/1aBq5ia9krF-7RYVw7RXrwHn20IONj1C5/view?usp=sharing)  

## Contributing
Contributions are welcome! Please open an issue or submit a pull request on GitHub.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
