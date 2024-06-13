# CLI-based Programming Assessment Platform

This project is a CLI-based programming assessment platform designed to streamline the process of setting up and evaluating programming assignments. The platform leverages Linux user management and directory structures to isolate user environments and manage assessment scripts.

## Features

- **User Management**: Create user accounts based on a predefined list.
- **Question Management**: Set up questions and test cases in designated directories.
- **Assessment Commands**: Evaluate public and private test cases for submitted assignments.

## Commands

### SET_ENV


Sets up the environment by copying questions, private test cases, public test cases, and executables to the respective directories:
- `/java_lab/Questions/`
- `/java_lab/private_test_case/`
- `/java_lab/public_test_case/`
- `/java_lab/executables/`

### CREATEUSER
Creates users from the `userlist.txt` file. Each user will have their own home directory.

### SETQUESTION
Copies the specified question file to the Java and Python folders within the `Programs` directory located in the home directory of each user.

### MAKE_DIR
Creates a `Programs` directory in the home directory of each user and sets up `Python` and `Java` subdirectories.

### EVALUATE
Assesses the public test cases for a given user's submission.

### SUBMIT
Assesses the private test cases for a given user's submission.

## Directory Structure

The platform uses a structured directory layout to organize questions and test cases:

/home/username/ <br>
├── Programs/ <br>
│ ├── Java/<br>
│ └── Python/<br>
/java_lab/<br>
├── Questions/<br>
├── private_test_case/<br>
├── public_test_case/<br>
└── executables/
## Usage

1. **Setup Environment**: Use the `SET_ENV` command to initialize the environment.
   ```bash
   ./SET_ENV

2. Create Users: Use the CREATEUSER command to create users from userlist.txt.
```commandline
./CREATEUSER <userlist.txt>
```
3. Set Questions: Use the **SETQUESTION** command to distribute a question file to all users.
```commandline
./SETQUESTION <path_to_question_file>
```

4. Make Directories: Use the MAKE_DIR command to create necessary directories in each user's home directory.
```commandline
./MAKE_DIR
```


--------------------------------------------------------------


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
...

### SUBMIT
...

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
