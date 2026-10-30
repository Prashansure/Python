filename = input()

try:
    if filename not in {"data.txt", "marks.txt", "log.txt"}:
        raise FileNotFoundError
    print("File opened successfully")

except FileNotFoundError:
    print("FileNotFoundError")