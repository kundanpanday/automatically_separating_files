import os
import shutil

# Prints all unique file extensions in the given directory and its subdirectories.
def print_unique_extensions(directory):
     if not os.path.exists(directory):  #if the directory does not exist leave function.
        print(f"Error: Directory '{directory}' not found.")
        return
     try:
        extensions = set()  
        for root, _, files in os.walk(directory):  
            for file in files: 
                extensions.add(os.path.splitext(file)[1])   # Add file extension to the set.
        print("Unique file extensions:", extensions)  
    except Exception as e:  # Catch any exceptions.
        print(f"Error listing files: {e}")   

# Organizes files by their extensions within their respective parent directories and prints the number of directories and files in them.
def organize_files_by_extension(directory):    
     if not os.path.exists(directory):
        return
    try:
        for root, _, files in os.walk(directory):  
            extension_dirs = {} 
            for file in files: 
                file_path = os.path.join(root, file)  # Construct the full file path.
                if os.path.isfile(file_path):   
                    _, extension = os.path.splitext(file)  # Split the filename and its extension.
                    if extension: 
                        target_dir = os.path.join(root, extension[1:])  # Create target directory name and remove the dot from the extension.
                        if target_dir not in extension_dirs: 
                            os.makedirs(target_dir, exist_ok=True)    # Create the directory if it doesn't exist.                        
                        shutil.move(file_path, os.path.join(target_dir, file))   # Move the file to the new directory.

        print("The Files are organized Successfully")  
    except Exception as e:
        print(f"Error organizing files: {e}") 

# Allow user to input the directory path
 directory_path = input("Enter the directory path to organize: ") # Get the path of the folder to be organized from user.

#Call the function to display all the unique file extensions and to organize the files based on extension.
print_unique_extensions(directory_path)  
organize_files_by_extension(directory_path)  
