# Building a CI/CD Pipeline for a Python Web App Using Github Actions and Docker BCP1-A
Building a CI/CD Pipeline for a Python Web App using GitHub Actions and Docker addresses the critical business need to reduce manual deployment effort while improve code quality &amp; early defect detection. Working within a scale-up company (50-150 employees), Xterns will develop a comprehensive solution that tackles real-world problems through hands-  

## 📂 Repository Structure

```text
├── .github/workflows/  # CI/CD Pipeline definitions
├── src/                # Main application logic
├── tests/              # Automated test suite
├── docs/               # Project documentation & strategies
├── .gitignore          # Excluded files and secrets
└── README.md           # Project overview and documentation
```

### Directory Details

- **​.github/workflows/**: Contains the GitHub Actions YAML files for the automated CI/CD pipeline.
- **​src/**: Contains the core Python application code and business logic.
- **​tests/**: Contains unit and integration tests to ensure code quality before deployment.
- **​docs/**: Stores project documentation, including the branching strategy and setup guides.
- **​.gitignore/**: Specifies intentionally untracked files that Git should ignore (e.g., __pycache__, .env).

---

## 🌿 Branching Strategy
This project follows a **main / dev / feature** branching model.

### Branch Overview
| Branch | Purpose | Protected |
| :--- | :--- | :--- |
| `main` | Production-ready code only | ✅ Yes |
| `dev` | Integration branch for completed features | ✅ Yes |
| `feature/*` | New features and bug fixes | ❌ No |

### Workflow
**1. Starting a new feature:**
```bash
git checkout dev
git pull origin dev
git checkout -b feature/your-feature-name
```
**2. Opening a Pull Request:**

*  Push your branch: git push origin feature/your-feature-name.

*  Target: Open a PR targeting dev (not main).

*  Review: Request at least one reviewer.

*  Checks: All CI checks must pass before merging.

*  Merge: Squash and merge to keep dev history clean.

**3. Releasing to Production:**

*  Open a PR from dev → main.

*  A lead reviews and approves.

*  Merge using a merge commit.

*  Tag the release: git tag v1.x.x && git push --tags.
---

## 🚀 CI/CD Pipeline Details

​The project utilizes **GitHub Actions** to ensure every change is tested before merging.

* **​Triggers**: The pipeline runs on every push and pull_request targeting the main branch.
* **​Workflow**:
    * **​Environment**: Runs on ubuntu-latest.
    * **Setup**: Configures Python 3.10. 
    * **Dependencies**: Installs pytest and requirements.
    * **Testing**: Executes pytest test_app.py to validate code logic.

## Prerequisites

To successfully set up, develop, and deploy this project, ensure you have the following:

* **Python 3.x & Virtualenv**: For local development and managing the Python web app environment.
* **Docker**: To containerize the application and build images for the CI/CD pipeline.
* **Git**: For version control and managing feature branches.
* **GitHub Account**: To host the repository and run the GitHub Actions workflows.
* **DockerHub Account**: To store and manage the Docker images built during the workflow.

## ⚙️ Local Setup
**1. Clone the repository**:
```bash
git clone [repository-url]
cd [project-folder-name]
```
**2. Create and activate a virtual environment**:
```bash
python -m venv venv

# On Windows:
venv\Scripts\activate

# On Mac/Linux:
source venv/bin/activate
```
**3. Install dependencies**:
```bash
pip install -r
requirements.txt
```
**4. Run tests**:
```bash
pytest
```

## Branching Strategy
Documentation for our branching strategy is currently being finalized and will be updated shortly.

## 👥 Contributing: Development Team (Xterns Batch 2)

This project is a collaborative effort by the following DevOps practitioners. Each member was responsible for a specific component of the infrastructure and automation pipeline.

| Contributor | Area of Responsibility |
| :--- | :--- |
| **@omomotoly** | Documentation & Main README |
| **@foladevops** | Branching Strategy & Documentation |
| **Ahmed Sheriffdeen Oluwatoyin** | CI/CD Workflow (`ci.yml`) |
| **Mary Olubusola Erinle-Adesina** | Python Unit Testing |
| **@habeebakorede** | Repository Structure & Folder Organization |
| **@steven.babarimisa** | Git Configuration & Branch Protection |
| **@alibras257** | Docker Configuration & Setup Instructions |
| **@sulazo112** | Python Virtual Environments & Local Runtime |
| **Olusegun Ayinla** | Requirements Management & Clean Install Testing |
| **@dimonjerry** | Setup Documentation |
| **@sabhayor** | End-to-End Pipeline Testing |
| **@samuelezra234** | Workflow Technical Documentation |
| **Akinwale Idowu** | Failure Scenarios & Notifications |
| **@bukola_salawu** | Code Review & PR Validation |