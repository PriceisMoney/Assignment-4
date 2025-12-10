# Write user input to the file ---

text_to_write = input("Enter text to write to the file: ")  # take user input
with open("output.txt", "w") as file:  # open file in write mode
    file.write(text_to_write + "\n")  # write content and add newline
print("Data successfully written to output.txt.\n")  # confirmation message


# Append additional text to the same file ---

additional_text = input("Enter additional text to append: ")  # take input for append
with open("output.txt", "a") as file:  # open in append mode
    file.write(additional_text + "\n")  # append content
print("Data successfully appended.\n")  # confirmation message


# Read and display final content ---

print("Final content of output.txt:")
with open("output.txt", "r") as file:  # open file in read mode
    content = file.read()  # read entire content
    print(content)  # display file content
