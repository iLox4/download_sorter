import os
import random
from setup import EXTENSIONS_MAP, DOWNLOAD_FOLDER_PATH, OTHER_FOLDER_PATH
from utils import move_file

files = os.listdir(DOWNLOAD_FOLDER_PATH)

for file in files:
    file_name, file_extension = os.path.splitext(file)

    # skips directories
    if not file_extension:
        continue

    target_folder_path = EXTENSIONS_MAP.get(file_extension.lower())

    # if extension is not define in the map -> it will move it to others folder
    if not target_folder_path:
        target_folder_path = OTHER_FOLDER_PATH
    
    if not os.path.exists(target_folder_path):
        os.makedirs(target_folder_path)

    target_file = target_folder_path + "/" + file
    # TODO: handle better files with the same name -> add counter or prompt to add new name
    if os.path.exists(target_file):
        file_name = file_name + "_" + random.randint(1, 100)
        target_file = target_folder_path + "/" + file_name + file_extension
    
    source_file = DOWNLOAD_FOLDER_PATH + "/" + file
    move_file(source_file, target_file)
    

    