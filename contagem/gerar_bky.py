import os
import csv
import zipfile
import glob

from contagem.analise_bky import analise_bky

# Diretório que será realizada a contagem dos blocos
folder_path = 'C:/Users/Elias/Documents/GitHub/app_inventor_analysis/modulo_doze'


# Lista de todos os arquivos zip
zip_files = glob.glob(os.path.join(folder_path, '**/*.zip'), recursive=True)

# Se existe ao menos um arquivo zip
if zip_files:
    # loop sobre todos os arquivos zip
    for zip_file in zip_files:
        zip_folder_path = os.path.dirname(zip_file)
        # Abre o arquivo zip
        with zipfile.ZipFile(zip_file, 'r') as myzip:
            # Lista de todos os arquivos no zip
            files_in_zip = myzip.namelist()
            
            # Encontrar arquvi .bky
            bky_files = [file for file in files_in_zip if file.endswith('.bky')]

            # Extrair o nome do arquivo do caminho completo
            zip_file_name = os.path.basename(zip_file)

            # Remover a extensão para ter apenas o nome
            zip_name_without_extension = os.path.splitext(zip_file_name)[0]

            folder_name = zip_name_without_extension

            # Combinar o caminho e o nome para criar o caminho completo do arquivo
            full_folder_path = os.path.join(zip_folder_path, folder_name)

            # Criar a pasta caso não exista
            if not os.path.exists(full_folder_path):
                os.makedirs(full_folder_path)
                print(f"Folder '{folder_name}' created in '{folder_path}'")

            # Se existe ao menos um arquivo .bky
            if bky_files:
                # Loop sobre todos os arquivos .bky
                for bky_file in bky_files:
                    # Abrir arquivo .bky
                    with myzip.open(bky_file) as myfile:
                        # Ler o conteúdo do arquivo .xml
                        xml_bky = myfile.read()

                    # Extrair o nome do arquivo do caminho completo e remover a extensão
                    bky_file_name = os.path.splitext(os.path.basename(bky_file))[0]

                    # Atribuindo nome ao csv
                    csv_filename = "results_" + bky_file_name + ".csv"

                    # Combinar caminho para pasta e nome do arquivo para gerar o caminho completo
                    csv_file_path = os.path.join(full_folder_path, csv_filename)

                    # Aplicar decode no formato utf-8
                    decoded_xml_bky = xml_bky.decode("utf-8")

                    data = analise_bky(decoded_xml_bky)

                    # Escrevendo dados no csv
                    with open(csv_file_path, mode='w', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerows(data)

                    #print(decoded_xml_bky)
                    print("\n")
                
                # Inicialização de dicionário para armazenar a soma de cada categoria de bloco
                pattern_sums = {}

                # Lista de todos os arquivos no diretório
                csv_files = [f for f in os.listdir(full_folder_path) if f.endswith('.csv')]

                # Loop em cada arquivo .csv
                for csv_filename_r in csv_files:
                    
                    if csv_filename_r == 'total.csv':
                        continue

                    csv_file_path_result = os.path.join(full_folder_path, csv_filename_r)
                    
                    with open(csv_file_path_result, mode='r') as file:
                        reader = csv.reader(file)
                        
                        # Iterar cada linha do arquivo .csv
                        for row in reader:
                            block, value = row
                            value = int(value)  # Converter o valor para inteiro
                            
                            if block in pattern_sums:
                                pattern_sums[block] += value
                            else:
                                pattern_sums[block] = value

                # Escrever a soma dos valores em um novo arquivo .csv final
                output_csv_path = full_folder_path + '/total.csv'

                with open(output_csv_path, mode='w', newline='') as file:
                    writer = csv.writer(file)
                    
                    # Escrever a soma dos valores
                    for block, total in pattern_sums.items():
                        writer.writerow([block, total])

            else:
                print(f"No XML files found in the zip file: {zip_file}")
else:
    print("No zip files found in the directory.")