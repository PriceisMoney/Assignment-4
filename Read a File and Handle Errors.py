import io

# Trying to open and read the file
try:
    print("Reading file content:\n")

    with open("sample.txt", "rt") as file:
        lines = file.readlines()

        line_number = 1  # starting line number
        for line in lines:  # simple loop
            print(f"Line {line_number}: {line.strip()}")
            line_number += 1  # increase line number manually

except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")

except io.UnsupportedOperation:
    print("Error: The file was opened in a mode that does not support reading.")
