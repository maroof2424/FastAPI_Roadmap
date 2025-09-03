import os

# Define directory structure
structure = {
    "Week05_Async_Background": {
        "app": [
            "__init__.py",
            "main.py",
            "endpoints.py",
            "db.py",
            "tasks.py",
            "utils.py"
        ],
        "tests": [
            "test_endpoints.py",
            "test_tasks.py"
        ],
        "requirements.txt": None,
        "README.md": None
    }
}

# Function to create directories and files
def create_structure(base, structure):
    for name, content in structure.items():
        dir_path = os.path.join(base, name)
        os.makedirs(dir_path, exist_ok=True)

        if isinstance(content, dict):
            create_structure(dir_path, content)
        elif isinstance(content, list):
            for file in content:
                file_path = os.path.join(dir_path, file)
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(f"# {file}\n")
        elif content is None:
            file_path = os.path.join(base, name)
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(f"# {name}\n")

# Run the function
base_dir = "."  # current dir
create_structure(base_dir, structure)

print("✅ Week05_Async_Background project structure created!")
