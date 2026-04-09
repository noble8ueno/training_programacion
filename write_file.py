# Create or open a file and write a message using try/except

file_name = "first_file.txt"

try:
    with open(file_name, "w") as file:
        file.write("Hello world this is my first file")

    print("File created and message written successfully.")

except IOError as e:
    print(f"File operation failed: {e}")

except Exception as e:
    print(f"Unexpected error: {e}")
