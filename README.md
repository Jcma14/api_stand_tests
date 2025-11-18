# Automated API Tests with Pytest

This project contains automated API tests written in Python using **Pytest** and the **Requests** library.  
The tests validate the `firstName` field when creating a new user through an API, checking both valid and invalid input.

---

## 🚀 How to Use

### 1. Install dependencies

```python
pip install pytest requests
```

### 2. Run all tests
```python
pytest
```
### 3. Run a specific file
```python
pytest test_create_user.py
```
### 4. Verbose mode
```python
pytest -v
```
## 🧪 What the Tests Check
* Successful user creation (201)
* Error responses (400) for:
* Too short or too long names
* Special characters
* Spaces
* Numbers
* Missing or empty fields
* Wrong data types
* User appears once in the users table after creation

## 📘 About This Project
This repository is part of my QA Engineering learning journey, where I practice building real automated API tests using Pytest and Python.