# Sample log data (instead of file)
logs = [
    "INFO User logged in",
    "WARNING Low battery",
    "ERROR File not found",
    "INFO Process started",
    "ERROR System crash"
]

error_count = 0
warning_count = 0
info_count = 0

# Process logs
for line in logs:
    if "ERROR" in line:
        error_count += 1
    if "WARNING" in line:
        warning_count += 1
    if "INFO" in line:
        info_count += 1

# Display result
print("Log Summary")
print("ERROR:", error_count)
print("WARNING:", warning_count)
print("INFO:", info_count)