import os

# Base path
base_path = "P:/Python/FastAPI_Roadmap"

# Week-wise structure (FIXED)
roadmap = {
    "Week01_Fundamentals": [
        "main.py",
        "README.md",
        "app/__init__.py",
        "app/routes.py",
        "app/models.py",
    ],
    "Week02_CRUD_Pydantic_Routers": [
        "main.py",
        "README.md",
        "app/__init__.py",
        "app/routers/posts.py",
        "app/models.py",
        "app/schemas.py",
        "app/crud.py",
    ],
    "Week03_Database_SQLAlchemy": [
        "main.py",
        "README.md",
        "app/__init__.py",
        "app/database.py",
        "app/models.py",
        "app/schemas.py",
        "app/crud.py",
        "app/routers/posts.py",
        "app/routers/users.py",
    ],
    "Week04_Authentication_JWT": [
        "main.py",
        "README.md",
        "app/__init__.py",
        "app/database.py",
        "app/models.py",
        "app/schemas.py",
        "app/crud.py",
        "app/routers/auth.py",
        "app/core/security.py",
    ],
    "Week05_Async_BackgroundTasks": [
        "main.py",
        "README.md",
        "app/__init__.py",
        "app/routers/tasks.py",
        "app/services/email.py",
        "app/services/external_api.py",
    ],
    "Week06_Testing_Env_Config": [
        "main.py",
        "README.md",
        ".env",
        "app/__init__.py",
        "app/config.py",
        "tests/test_auth.py",
        "tests/test_posts.py",
    ],
    "Week07_Docker_Deployment": [
        "main.py",
        "README.md",
        "Dockerfile",
        "docker-compose.yml",
        "app/__init__.py",
        "app/main.py",
    ],
    "Week08_CICD_Performance": [
        "main.py",
        "README.md",
        ".github/workflows/ci.yml",
        "app/__init__.py",
        "app/logging_config.py",
        "app/monitoring/metrics.py",
    ]
}

# Create directories and files
for week, files in roadmap.items():
    week_dir = os.path.join(base_path, week)
    os.makedirs(week_dir, exist_ok=True)
    for file in files:
        file_path = os.path.join(week_dir, file)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w') as f:
            f.write(f"# {os.path.basename(file)}\n")

# Create README.md in base dir
base_readme_path = os.path.join(base_path, "README.md")
with open(base_readme_path, 'w') as f:
    f.write("# FastAPI Roadmap\n")
