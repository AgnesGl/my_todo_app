#tu dam stała nazwę pliku, i jak bym go kiedyś zmieniła,
#to wystarczy wpisać poniżej nową nazwę
FILEPATH = "todos.txt"
#zapiszę definicje tego, co mi się powtarza w kodzie
#otwieram file, czytam linie, zamyka się automatycznie, bo jest "with")
"""def get_todos():
    with open("todos.txt", "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local"""
#zamiast zdefiniować z góry źrodło, piszę tylko 'filepath', a potem w kodzie dopiero konkretnie
def get_todos(filepath = FILEPATH):
    """Read a text file and return the list of
    to-do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath = FILEPATH):
    """Write the to-do items list in the text file."""
    with open(filepath, "w") as file:
        file.writelines(todos_arg)
    #tu nic nie ma nic return, tylko robi to pisanie

#to jest executed tylko kiedy functions.py jest run directly
if __name__ == "__main__":
    print("Hello")
    print(get_todos())