import os
import shutil

from_dir = "Downloads"
to_dir = "Arquivos_Documentos"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)
    
    # Se a extensão estiver em branco, continue para o próximo arquivo
    if extension == "":
        continue
    
    # Verificar se a extensão está na lista de extensões desejadas
    if extension in ['.txt', '.doc', '.docx', '.pdf']:
        path1 = from_dir + '/' + file_name
        path2 = to_dir + '/' + extension[1:].upper()  # Criar uma nova pasta com o nome da extensão
        path3 = path2 + '/' + file_name
        
        # Verificar se o caminho de destino existe
        if os.path.exists(path2):
            print("Movendo", file_name)
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print("Movendo", file_name)
            shutil.move(path1, path3)
