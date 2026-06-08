# CI/CD Python Application Project

This repository contains a containerized Python application with an automated CI/CD pipeline.

## 🛠️ Setup Instructions

### Prerequisites
* **Python 3.10+**
* **Docker**
* **Git**

### Local Installation
1. Clone the repository and navigate to the project directory:
   ```bash
   git clone <your-repository-url>
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 How to Run the Application

### Running Locally
To launch the application directly using Python:
```bash
python src/app.py
```

### Running with Docker
Since the project uses a standard standalone configuration, build and run the container directly using the `Dockerfile`:
```bash
# 1. Build the Docker image
docker build -t my-app .

# 2. Run the container mapping the application port
docker run -p 5000:5000 my-app
```

### Running Tests
Execute the automated test suite locally:
```bash
pytest
```

---

## 🌿 Branching Strategy & Git Workflow

### 1. Main Branch (`main`)
* Represents stable, production-ready code.
* Direct pushes to `main` are restricted.

### 2. Feature Branches (`feature/`)
* All development and bug fixes must happen on a dedicated branch.
* Follow the naming convention: `feature/<branch-name>` (e.g., `feature/final-fixes`).