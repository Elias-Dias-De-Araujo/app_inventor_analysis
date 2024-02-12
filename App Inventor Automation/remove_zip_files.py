import os
import glob

# Function to remove all zip files in a directory and its subdirectories
def remove_zip_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".zip"):
                file_path = os.path.join(root, file)
                os.remove(file_path)
                print(f"Deleted: {file_path}")

# Specify the directory where you want to remove zip files
directory_to_search = 'C:/Users/elias/Desktop/www/fdr_projecsts'

# Call the function to remove zip files
remove_zip_files(directory_to_search)