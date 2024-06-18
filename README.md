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
   - [Set Questions](#set-questions)
   - [Make Directories](#make-directories)
   - [Evaluate Submissions](#evaluate-submissions)
6. [Example Workflow](#example-workflow)
7. [Contributing](#contributing)
8. [License](#license)

## Introduction
This project is a CLI-based programming assessment platform designed to streamline the process of setting up and evaluating programming assignments. The platform leverages Linux user management and directory structures to isolate user environments and manage assessment scripts.

## Features
...

## Commands
...

### SET_ENV
Before Executing `Set_Env` Command. Admin (or) Host Should Create the Directory in root folder (/) as this [Directory Structure](#program-lab-directory).<br>
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

`SUBMIT` command logs the submission information in the log file located in `/var/log/program_labs`. Log file consist of the information about the username, time, programming language used, program name, passed test case count, failed test case count, runtime. Log file stores these information in CSV (Comma Seperated Value) Format.

## Directory Structure
### Admin home Directory
/home/user<br>
├── project/ <br>
│ ├── Createuser<br>
│ └── MakeDir<br>
│ └── SetEnv<br>
│ └── SetQuestion<br>

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
...

### Setup Environment
...

### Create Users
...

### Set Questions
...

### Make Directories
...

### Evaluate Submissions
...

## Example Workflow
...

## Contributing
...

## License
...
