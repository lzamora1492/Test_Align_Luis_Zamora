
# 🧪 SDET Evaluation - Luis Zamora Campos

This project automates the functional tests for the UI web application. It was developed wwith: **Python**, **Selenium WebDriver** and **Pytest**, it covers test cases like login, navegation/basic accions and Bonus.

---

## 🧰 Technologies and tools used

- Python 3.13.3
- Selenium WebDriver
- Pytest
- Pytest-html
- Pytest-metadata
- Page Object Model (POM)
- Git
- Git Bash

---

## 📁 Project structure

```
Test_Align_Luis_Zamora/
├── pages/
│   ├── login_page.py
├── reports/
│   ├── Test_report_Luis_Zamora.html
└── README.md
├── conftest.py
├── test_1_login.py
├── test_2_navigation.py
├── test_3_bonus.py

```
Notes:
The reports folder will be created when the test cases will run for first time

---

## ✅ Prerequisites

- Python 3.13.3
- Selenium WebDriver
- Pytest
- Pytest-html
- Google Chrome 136.X
- Chromedriver configurado en el PATH

## 🔧 Installation guide

```git bash
Move to the directory where you want to download the project

git clone git remote add origin https://github.com/lzamora1492/Test_Align_Luis_Zamora.git
cd Test_Align_Luis_Zamora
```
---

## ⚙️ Configuration

The OS used for projet was Windows.

Checked if you have python install in the OS (Run the following command in the terminal: python --version)
	If you have it installed continue with the step 2, Otherwise install it download it from (https://www.python.org/downloads/)

Install the following libraries: selenium, pytest, pytest-html (Commands to run in the OS terminal: pip install <library_name>)

---

## 🚀 Test execution

### Execute todas las pruebas

Open the OS terminal
Move to the directory where the project was downloaded (ex: Desktop)

```bash
pytest -v Test_Align_Luis_Zamora/ --html=Test_Align_Luis_Zamora/reports/Test_report_Luis_Zamora.html --self-contained-html
```
Notes: 
It will create a report test in the report folder of the project