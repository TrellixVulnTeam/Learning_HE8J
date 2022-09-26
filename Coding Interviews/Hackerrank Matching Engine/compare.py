
# Importing difflib
import difflib
  
with open('input.txt') as file_1:
    file_1_text = file_1.readlines()
  
with open('input2.txt') as file_2:
    file_2_text = file_2.readlines()
  
# Find and print the diff:
with open('diff.txt', 'w') as file_out:
    for line in difflib.unified_diff(
            file_1_text, file_2_text, fromfile='file1.txt', 
            tofile='file2.txt', lineterm=''):
        file_out.write(line)