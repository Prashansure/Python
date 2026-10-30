def backup_files(folder, path=""):
    for name, content in folder.items():
        if isinstance(content, dict):
            # If folder, call recursion
            backup_files(content, path + name + "/")
        else:
            # If file, print path
            print(path + name)

# Sample folder structure
file_system = {
    "Documents": {
        "file1.txt": None,
        "file2.txt": None
    },
    "Images": {
        "photo1.jpg": None,
        "Vacation": {
            "photo2.jpg": None
        }
    }
}

# Function call
backup_files(file_system)