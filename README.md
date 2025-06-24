# PlagiaGuard 🚫📄

**AI-Powered Code Plagiarism Detector**

PlagiaGuard is a smart system designed to detect plagiarism in programming assignments by analyzing the logic of the code, not just its syntax. It uses Abstract Syntax Trees (AST), semantic similarity (embeddings), and GitHub code matching to identify potential plagiarism even when the code is slightly modified.

---

## 🔍 Features

- 🔎 **Logic-level plagiarism detection** using AST comparison
- 🧠 **AI-based semantic similarity scoring** with Sentence Transformers
- 🌐 **Online match detection** via GitHub Search API
- 📊 **Similarity score generation** and result reporting
- 💡 Designed for educators, institutions, and coding platforms

---

## 🛠️ Tech Stack

| Layer        | Tools / Frameworks         |
|--------------|-----------------------------|
| Frontend     | HTML & CSS                   |
| Backend      | Python, FastAPI (optional)    |
| Code Analysis| Python `ast`, `difflib`     |
| AI/ML        | Sentence Transformers        |
| External API | GitHub Code Search API       |

---

## 👀 Preview
<img src="https://private-user-images.githubusercontent.com/132296372/458247416-0299fcf6-5309-43e8-b2c0-4950bdfef5aa.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTA3NTAwOTAsIm5iZiI6MTc1MDc0OTc5MCwicGF0aCI6Ii8xMzIyOTYzNzIvNDU4MjQ3NDE2LTAyOTlmY2Y2LTUzMDktNDNlOC1iMmMwLTQ5NTBiZGZlZjVhYS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNjI0JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDYyNFQwNzIzMTBaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0wYTVkY2ExN2VlMzEwYzNmMGRiM2UxOWEwODI2MmQ3ZTIyZmFmZTgzMDQ0NThmOTE3YWE2MzhjOWIwZTI1NDRkJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.uDoN3xGu_T7awKCLt8J-ujqozR46KY8OVnFb3SU95uo" width="1000" alt="Home Page"> <img src="https://private-user-images.githubusercontent.com/132296372/458247415-8f303190-9876-4b96-901d-80388b6f33da.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTA3NTAwOTAsIm5iZiI6MTc1MDc0OTc5MCwicGF0aCI6Ii8xMzIyOTYzNzIvNDU4MjQ3NDE1LThmMzAzMTkwLTk4NzYtNGI5Ni05MDFkLTgwMzg4YjZmMzNkYS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNjI0JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDYyNFQwNzIzMTBaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT01ZTg2MDE1NTEzYTZhOTdjNDczOTZmODIyZDg4MGU0ZGY0NDQ4YjU4OTIwNjg1YjVkY2IxZjk0YzNjOWM1MzE3JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.gdFDzZYPrhQ0txCAJ_nR5dPDjHH9XJOT_7EPWCdi5S8" width="1000" alt="Result Page">

---

## 🔁 Workflow

1. User submits a code file.
2. Code is parsed into an AST (Abstract Syntax Tree).
3. Semantic embeddings are generated and compared.
4. GitHub is queried for potential code matches.
5. A similarity score and feedback report are generated.

---

## 📂 Project Structure

```bash
PlagiaGuard/
├── static/           # Static files 
│   ├── style.css
│   └── table.css
├── templates/             # HTML templates
│   ├── home.html         # Homepage
│   ├── table.html        # Results
├── app.py                # Main FastAPI app
├── src                   # Source Python File
│    ├── model.py          # Core logic for AST + embeddings
├── Notebooks             # Notebook
│   ├── logic.ipynb       # Logic created Notebook
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

## 🚀 Getting Started
1. Clone the Repo
```bash
git clone https://github.com/TAK-PRAVEEN/PlagiaGuard.git
cd PlagiaGuard
```
2. Install Dependencies
```bash
pip install -r requirements.txt
```
3. Run the App
```bash
python app.py
```

OR

```bash
uvicorn app:app --reload
```

---

## 📊 Use Cases
- 👩‍🏫 Educators – check student submissions for originality

- 🧑‍💻 Coding platforms – ensure assignment integrity

- 🏢 Recruiters – validate test submissions in hiring

---

## 🔐 Disclaimer
PlagiaGuard is a research/educational project. It does not guarantee 100% accuracy and should be used as a support tool alongside human judgment.

---

## 🙌 Contributors
Praveen Tak – <a href="https://www.linkedin.com/in/praveen-tak-50b669272/" target="_blank">LinkedIn Profile</a>

Team: Hash Splinters

---

## 📄 License
This project is open-source and available under the MIT License.

