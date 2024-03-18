import re
import os
import shutil
import zipfile

# Diretório que ficará com as submissões válidas
root_directory = 'C:/Users/Elias/Documents/GitHub/app_inventor_analysis/modulo_oito'

# Diretório que ficará com as submissões inválidas ( O script cuidará de sua criação )
destination_directory = 'C:/Users/Elias/Documents/GitHub/app_inventor_analysis/modulo_oito_not_accepted'

pattern = r'\d+'

# Removendo sufixo de "_assignsubmission_file_" do nome das pastas
# Verificar todos os itens no diretório
for filename in os.listdir(root_directory):
    # Checar se o item é uma pasta
    if os.path.isdir(os.path.join(root_directory, filename)):
        # Checar se o nome do item contém "_assignsubmission_file_"
        if "_assignsubmission_file_" in filename:
            # Gerar o novo nome ao remover "_assignsubmission_file_"
            new_name = filename.replace("_assignsubmission_file_", "")
            # Renomeando pasta
            os.rename(os.path.join(root_directory, filename), os.path.join(root_directory, new_name))
            print(f"Renamed folder from '{filename}' to '{new_name}'")

# Função para modificar nome de diretório
def change_directory_name(folder_path, suffix):
    match = re.search(pattern, folder_path)
    extracted_number = match.group(0)
    new_folder_name = os.path.join(os.path.dirname(folder_path),  extracted_number + suffix)
    os.rename(folder_path, new_folder_name)
    print(f"Renamed folder '{folder_path}' to '{extracted_number + suffix}'")

# Função para converter arquivos .aia para .zip
def convert_aia_to_zip(folder_path):
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.aia'):
                aia_file_path = os.path.join(root, file)
                zip_file = aia_file_path.replace('.aia', '.zip')
                shutil.move(aia_file_path, zip_file)

# Função para verificar todas as pastas no diretório root
for dirpath, dirnames, _ in os.walk(root_directory):
    for dirname in dirnames:
        folder_path = os.path.join(dirpath, dirname)
        # Checar se a pasta contém arquivos .aia
        if any(filename.endswith('.aia') for filename in os.listdir(folder_path)):
            convert_aia_to_zip(folder_path)
            # Renomear a pasta para "<matricula_aluno>_contain_aia"
            change_directory_name(folder_path, "_contain_aia")
            #print(f"Converted .aia files in '{folder_path}' to .zip")
        else:
            if any(filename.endswith('.zip') for filename in os.listdir(folder_path)):
                # Renomear a pasta para "<matricula_aluno>_contain_aia"
                change_directory_name(folder_path, "_contain_zip")
            else:
                # Renomear a pasta para "<matricula_aluno>_not_contain_aia"
                change_directory_name(folder_path, "_not_contain_aia")

print("Conversion complete.")


# Verificar todos os itens ( pastas e arquivos ) no diretório root
for item in os.listdir(root_directory):
    item_path = os.path.join(root_directory, item)

    # Checar se o item é uma pasta
    if os.path.isdir(item_path):

        # Checar se o nome da pasta contém "_not_contain_aia"
        if "_not_contain_aia" in item:

            # Construir caminho de destino
            destination_path = os.path.join(destination_directory, item)

            # Mover o diretório para o caminho de destino
            shutil.move(item_path, destination_path)

print("Folders moved successfully.")