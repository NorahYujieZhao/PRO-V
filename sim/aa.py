# Read all files from directories 1, 4, 18, 48, 64, 68, 96, 109, 15, 123, 124, 130 in output_tb_gen_tb_20250406 and create new folders
import os
import shutil

# Define directories to process
directories = ['1', '4', '18', '48', '64', '68', '96', '109', '15', '123', '124', '130']

# Iterate through each directory
for dir in directories:
    # Build source file path
    source_path = os.path.join('output_tb_gen_tb_20250406', dir)
    
    # Build target file path
    target_path = os.path.join('testcase', dir)
    
    # Create target folder
    os.makedirs(target_path, exist_ok=True)
    
    # Copy files
    if os.path.exists(source_path):
        for file in os.listdir(source_path):
            source_file = os.path.join(source_path, file)
            target_file = os.path.join(target_path, file)
            shutil.copy2(source_file, target_file)

