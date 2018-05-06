import os, glob, re # Imports python modules
from configparser import ConfigParser

def generate_data_file_list(battletech_home):
    streaming_assets = os.path.join(battletech_home, 'BattleTech_Data', 'StreamingAssets')
    data_directory = os.path.join(streaming_assets, 'data') #This needs to be stepped back to just StreamingAssets
    #Not sure how the below line works so I can't change it without breaking things.
    files = [os.path.join(os.path.relpath(directory_path, streaming_assets), filename) for directory_path, directory_names, filenames in os.walk(data_directory) for filename in filenames]
    files.sort()
    return files

def write_file_list(filename, filelist):
    with open(filename, 'w') as file:
        for filename in filelist:
            file.write(filename+'\n')

if __name__ == "__main__":
    config = ConfigParser()
    config.read('config.ini')
    battletech_home = config.get('directories', 'battletech_home')
    data_filelist = generate_data_file_list(battletech_home)
    write_file_list('defaultTree.txt', data_filelist)