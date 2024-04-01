# File Creation
try:
    # Open "my_file.txt" in write mode ('w')
    with open("my_file.txt", 'w') as file:
        # Write three lines of text to the file
        file.write("Line 1: This is the first line of text.\n")
        file.write("Line 2: 12345\n")
        file.write("Line 3: Hello, world!\n")
    print("File created successfully and initial content written.")
except Exception as e:
    print("Error occurred while creating the file:", e)
finally:
    print("File creation process completed.\n")

# File Reading and Display
try:
    # Open "my_file.txt" in read mode ('r')
    with open("my_file.txt", 'r') as file:
        # Read and display the contents of the file
        print("Contents of my_file.txt:")
        print(file.read())
except Exception as e:
    print("Error occurred while reading the file:", e)
finally:
    print("File reading process completed.\n")

# File Appending
try:
    # Open "my_file.txt" in append mode ('a')
    with open("my_file.txt", 'a') as file:
        # Append three additional lines of text to the existing content
        file.write("Line 4: Additional line 1\n")
        file.write("Line 5: Additional line 2\n")
        file.write("Line 6: Additional line 3\n")
        
    print("Content appended to my_file.txt successfully.")
except Exception as e:
    print("Error occurred while appending to the file:", e)
finally:
     print("File appending process completed.")
     
