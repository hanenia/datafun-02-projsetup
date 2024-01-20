"""Project 2: Creating folders"""

import pathlib
import math
import time
import Hanna__utils

"""Creat folders for a given range of years."""
def create_folders_for_range(Start, end):
    
    for year in range (Start, end + 1 ):
         folder_path = pathlib.Path(f'year_{year}')
         folder_path.mkdir(exist_ok=True)


"""Create Prefixed folders"""
def create_prefixed_folders(folders_list, prefix):
     
    for item in folders_list: 
          folder_path = pathlib.Path(f'{prefix}{item}')
          folder_path.mkdir(exist_ok=True)
		  
""" Create folders from list """
def create_folders_from_list(folder_list):
    for folder_name in folder_list:
        path = pathlib.Path(folder_name)
        path.mkdir(exist_ok=True)
		  
""" Create prefixed folders"""
def create_prefixed_folders(folder_list, prefix):
    
    for folder_name in folder_list:
        folder = pathlib.Path(prefix + folder_name)
        folder.mkdir(parents=True, exist_ok=True)



"""Creat folders periodically using a while loop"""
def create_folders_periodically(duration):
    
     counter=0
     while counter<5:
          folder_path = pathlib.Path(f'Folder_{counter}')
          folder_path.mkdir(exist_ok=True)
          counter += 1
          time.sleep(duration)

""" Create folders periodically """		  
def create_folders_periodically(duration):
    
    num_folders = 5 
    folder_count = 1

    while folder_count <= num_folders:
        pathlib.Path("folder-" + str(folder_count)).mkdir(exist_ok=True)
        folder_count += 1
        time.sleep(duration)


def main ():
     """Main function to demostrate module is capabilities"""

     create_folders_for_range(2010,2019)
     folder_names = ['data-csv', 'data-excel,' 'data-json']
     create_folders_for_list(folder_names)
     prefix = 'data-'
     create_prefixed_folders(folder_names, prefix)

     create_folders_periodically(5)

if __name__== '__main__':
    main()
     
    
