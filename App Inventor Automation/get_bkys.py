import os
import csv
import zipfile
import glob

from automation_app_inventor import analise_bky

folder_path = 'C:/Users/Elias/Documents/GitHub/app_inventor_analysis/modulo_oito'

# Get a list of all zip files in the directory
#zip_files = glob.glob('C:/Users/elias/Desktop/www/fdr_projecsts/*.zip')
zip_files = glob.glob(os.path.join(folder_path, '**/*.zip'), recursive=True)

# If there's at least one zip file
if zip_files:
    # Loop over all zip files
    for zip_file in zip_files:
        zip_folder_path = os.path.dirname(zip_file)
        # Open the zip file
        with zipfile.ZipFile(zip_file, 'r') as myzip:
            # Get a list of all files in the zip
            files_in_zip = myzip.namelist()
            
            # Find the bky file
            bky_files = [file for file in files_in_zip if file.endswith('.bky')]

            # Extract the file name from the full path
            zip_file_name = os.path.basename(zip_file)

            # Remove the file extension to get just the name
            zip_name_without_extension = os.path.splitext(zip_file_name)[0]

            folder_name = zip_name_without_extension

            # Combine the path and name to create the full folder path
            full_folder_path = os.path.join(zip_folder_path, folder_name)

            # Create the folder if it doesn't exist
            if not os.path.exists(full_folder_path):
                os.makedirs(full_folder_path)
                print(f"Folder '{folder_name}' created in '{folder_path}'")

            # If there's at least one xml file
            if bky_files:
                # Loop over all xml files
                for bky_file in bky_files:
                    # Open the xml file
                    with myzip.open(bky_file) as myfile:
                        # Read the content of the xml file
                        xml_bky = myfile.read()

                    # Extract the bky name from the full path and remove file extension
                    bky_file_name = os.path.splitext(os.path.basename(bky_file))[0]

                    # Atribuindo nome ao csv
                    csv_filename = "results_" + bky_file_name + ".csv"

                    # Combine folder path and file name to create the full file path
                    csv_file_path = os.path.join(full_folder_path, csv_filename)

                    # deoce from byte literal
                    decoded_xml_bky = xml_bky.decode("utf-8")

                    data = analise_bky(decoded_xml_bky)

                    # Escrevendo dados no csv
                    with open(csv_file_path, mode='w', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerows(data)

                    #print(decoded_xml_bky)
                    print("\n")
                
                # Initialize a dictionary to store the sums for each pattern category
                pattern_sums = {}

                # List all files in the directory
                csv_files = [f for f in os.listdir(full_folder_path) if f.endswith('.csv')]

                # Loop through each CSV file
                for csv_filename_r in csv_files:
                    
                    if csv_filename_r == 'total.csv':
                        continue

                    csv_file_path_result = os.path.join(full_folder_path, csv_filename_r)
                    
                    with open(csv_file_path_result, mode='r') as file:
                        reader = csv.reader(file)
                        
                        # Iterate through each row in the CSV file
                        for row in reader:
                            block, value = row
                            value = int(value)  # Convert the value to an integer
                            
                            if block in pattern_sums:
                                pattern_sums[block] += value
                            else:
                                pattern_sums[block] = value

                # Write the summed values to a new CSV file
                output_csv_path = full_folder_path + '/total.csv'

                with open(output_csv_path, mode='w', newline='') as file:
                    writer = csv.writer(file)
                    
                    # Write summed values
                    for block, total in pattern_sums.items():
                        writer.writerow([block, total])

            else:
                print(f"No XML files found in the zip file: {zip_file}")
else:
    print("No zip files found in the directory.")