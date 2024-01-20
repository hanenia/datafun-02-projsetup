""" Start a data analytics project """

import pathlib

def create_project_directory(directory_name: str): # add type
    """
    adding things
    """
    pathlib.Path(directory_name).mkdir(exist_ok=True)

def main():
    create_project_directory(directory_name='test') # name the parameter
    create_project_directory(directory_name='patient') # name the parameter
    

if __name__ == '__main__':
    main()


    
