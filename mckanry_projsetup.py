'''This project will create folders if not already created.'''

import pathlib

def create_project_directory(directory_name: str):
    '''
    Create a project sub-directory
    '''
    
    pathlib.Path(directory_name).mkdir(exist_ok=True)
    
def main():
    create_project_directory(directory_name='test')
    create_project_directory(directory_name='docs')
    
main()    