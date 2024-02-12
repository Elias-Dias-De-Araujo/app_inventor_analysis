import re
import os
import shutil
import zipfile

# Define the directory path where you want to search for folders
root_directory = 'C:/Users/Elias/Documents/GitHub/app_inventor_analysis/modulo_oito'
destination_directory = 'C:/Users/Elias/Documents/GitHub/app_inventor_analysis/modulo_oito_not_accepted'

pattern = r'\d+'

# Removing the sufix "_assignsubmission_file_"
# Iterate over all items in the directory
for filename in os.listdir(root_directory):
    # Check if the item is a directory
    if os.path.isdir(os.path.join(root_directory, filename)):
        # Check if the folder name contains "_assignsubmission_file_"
        if "_assignsubmission_file_" in filename:
            # Generate the new name by removing "_assignsubmission_file_"
            new_name = filename.replace("_assignsubmission_file_", "")
            # Rename the folder
            os.rename(os.path.join(root_directory, filename), os.path.join(root_directory, new_name))
            print(f"Renamed folder from '{filename}' to '{new_name}'")

def change_directory_name(folder_path, suffix):
    match = re.search(pattern, folder_path)
    extracted_number = match.group(0)
    new_folder_name = os.path.join(os.path.dirname(folder_path),  extracted_number + suffix)
    os.rename(folder_path, new_folder_name)
    print(f"Renamed folder '{folder_path}' to '{extracted_number + suffix}'")

# Function to convert .aia files to .zip files
def convert_aia_to_zip(folder_path):
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.aia'):
                aia_file_path = os.path.join(root, file)
                zip_file = aia_file_path.replace('.aia', '.zip')
                shutil.move(aia_file_path, zip_file)

# Verify all folders inside the root directory
for dirpath, dirnames, _ in os.walk(root_directory):
    for dirname in dirnames:
        folder_path = os.path.join(dirpath, dirname)
        # Check if the folder contains .aia files
        if any(filename.endswith('.aia') for filename in os.listdir(folder_path)):
            convert_aia_to_zip(folder_path)
            change_directory_name(folder_path, "_contain_aia")
            #print(f"Converted .aia files in '{folder_path}' to .zip")
        else:
            # Rename the folder to "<matricula_aluno>_not_contain_aia"
            if any(filename.endswith('.zip') for filename in os.listdir(folder_path)):
                change_directory_name(folder_path, "_contain_zip")
            else:
                change_directory_name(folder_path, "_not_contain_aia")

print("Conversion complete.")


# Iterate through all items (folders and files) in the source directory
for item in os.listdir(root_directory):
    item_path = os.path.join(root_directory, item)

    # Check if the item is a directory
    if os.path.isdir(item_path):

        # Check if the directory name contains "_not_contain_aia"
        if "_not_contain_aia" in item:

            # Construct the destination path
            destination_path = os.path.join(destination_directory, item)

            # Move the directory to the destination
            shutil.move(item_path, destination_path)

print("Folders moved successfully.")