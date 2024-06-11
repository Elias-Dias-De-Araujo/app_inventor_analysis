import os
import glob

# Função para remover todos os arquivos zip em um diretório e em seus subdiretórios
def remove_zip_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".zip"):
                file_path = os.path.join(root, file)
                os.remove(file_path)
                print(f"Deleted: {file_path}")

# Diretório para efetuar a remoção dos arquivos zip
directory_to_search = 'C:/Users/elias/Desktop/www/fdr_projecsts'

# Chamada de função para remover os arquivos zip
remove_zip_files(directory_to_search)