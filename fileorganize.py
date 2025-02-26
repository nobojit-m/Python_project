import os
import shutil

def organize_files():
    # Get the current directory where the script is located
    current_dir = os.getcwd()
    
    # Get all files in the current directory
    files = os.listdir(current_dir)
    
    # Process each file
    for file in files:
        # Skip the python script itself
        if file == os.path.basename(__file__):
            continue
            
        # Skip if it's not a file
        if not os.path.isfile(file):
            continue
            
        # Get the file extension
        file_extension = os.path.splitext(file)[1]
        
        # Skip if file has no extension
        if not file_extension:
            continue
            
        # Remove the dot from extension (e.g., '.txt' becomes 'txt')
        extension = file_extension[1:]
        
        # Create folder for this extension if it doesn't exist
        if not os.path.exists(extension):
            os.makedirs(extension)
            
        # Move the file to the corresponding folder
        try:
            shutil.move(file, os.path.join(extension, file))
            print(f"Moved {file} to {extension} folder")
        except Exception as e:
            print(f"Error moving {file}: {e}")

if __name__ == "__main__":
    print("Starting to organize files...")
    organize_files()
    print("Done organizing files!")
