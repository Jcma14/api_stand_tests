<!-- PROJECT BANNER -->
<p align="center">
  <img src="https://img.shields.io/badge/API%20Testing-Pytest-blue?style=for-the-badge&logo=python" alt="API Testing Badge"/>
  <img src="https://img.shields.io/badge/QA%20Engineer-Learning-orange?style=for-the-badge" alt="QA Learning Badge"/>
</p>

<h1 align="center">Automated API Tests with Pytest</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.14-blue?logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Pytest-Framework-green?logo=pytest"/>
  <img src="https://img.shields.io/badge/Requests-Library-orange?logo=python"/>
  <img src="https://img.shields.io/badge/Project-Active-success"/>
  <img src="https://img.shields.io/github/last-commit/Jcma14/api_stand_tests"/>
  <img src="https://img.shields.io/github/repo-size/Jcma14/api_stand_tests"/>
</p>

---

## Table of Contents

- [About the Project](#about-the-project)
- [How to Use](#how-to-use)
- [What the Tests Check](#what-the-tests-check)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Author](#author)

---

## About the Project

This project contains automated API tests written in Python using **Pytest** and the **Requests** library.  
The tests validate the `firstName` field when creating a new user through an API, checking both valid and invalid input.

---

## How to Use

### 1. Install dependencies

```bash
pip install pytest requests
```
### 2. Run all tests
```bash
pytest
```
### 3. Run a specific file
```bash
pytest test_create_user.py
```
### 4. Verbose mode
```bash
pytest -v
```
---

## What the Tests Check
* Successful user creation (201)
* Error responses (400) for:
* Too short or too long names
* Special characters
* Spaces
* Numbers
* Missing or empty fields
* Wrong data types
* User appears once in the users table after creation

---
 
## Project Structure
```text
api_stand_tests/
│── README.md
│── configuration.py
│── create_user_test.py
│── data.py
│── sender_stand_request.py
```

---

## Technologies Used
* Python 3.14.0
* Pytest for automated testing
* Requests for API communication
* Pycharm as the development environment
* Git & GitHub for version control

---

## Author
Camilo — QA Engineer in Training
This repository is part of my QA Engineering learning journey, where I practice building real automated API tests using Pytest and Python.

Learning API testing, automation, and software quality.

If you want to connect:

<p align="left">
  <a href="https://github.com/Jcma14">
    <img src="https://img.shields.io/badge/GitHub-Profile-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub Badge"/>
  </a>
  <br>
    <a href="https://www.linkedin.com/in/camilo-morales-qa/">
    <img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn Badge"/>
  </a>
</p>
