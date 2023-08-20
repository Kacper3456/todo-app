Filepath='todos.txt'
def get_todos(filepath=Filepath):
    """Read the textfile and return the list of to-do items"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local
def write_todos(todos_arg,filepath=Filepath):
    "write to-do items list into textfile"
    with open(filepath,'w') as file:
        file.writelines(todos_arg)