import os

# Define folder and files
structure = {
    "Week06_Testing_Configs": {
        "app": ["__init__.py", "main.py", "config.py"],
        "tests": [
            "__init__.py",
            "conftest.py",
            "test_basic.py",
            "test_users.py",
            "test_posts.py",
            "test_auth.py",
        ],
        "root_files": [".env", ".env.test", "pytest.ini"],
    }
}

def create_structure(base_path="."):
    for root, content in structure.items():
        root_path = os.path.join(base_path, root)
        os.makedirs(root_path, exist_ok=True)

        # app directory
        app_path = os.path.join(root_path, "app")
        os.makedirs(app_path, exist_ok=True)
        for f in content["app"]:
            open(os.path.join(app_path, f), "w").close()

        # tests directory
        tests_path = os.path.join(root_path, "tests")
        os.makedirs(tests_path, exist_ok=True)
        for f in content["tests"]:
            open(os.path.join(tests_path, f), "w").close()

        # root files
        for f in content["root_files"]:
            open(os.path.join(root_path, f), "w").close()

    print(f"✅ Project structure created inside {base_path}/Week06_Testing_Configs")

if __name__ == "__main__":
    create_structure()
