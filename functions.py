FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):        # filepath is the parameter, and a default parameter
    """ Read a text file and return the list of
        to-do items.
    """                                           # print(help(get_todos)), this is a docstring
    # NOTE 1
    # NOTE 2
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    # !return gives an instance of the LIST CLASS, not the list itself!
    # list is a type but can be called as class, they are interchangeable terms
    # distinction between classes (type) and the instances that these classes create
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH, ):  # non-default parameter always comes before default one
    """ Write the to-do items list in the text file."""
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello")

"""
NOTE 1: if we need absolute path: file = open(r"C:/whatever/todos.txt", "r") (backslash!)
        r at the beginning will ignore special characters (\r \n etc)

NOTE 2: without with-context manager: 
    file = open("files/todos.txt", "r")
    todos = file.readlines()
    file.close()

    file = open("files/todos.txt", "w")
    file.writelines(todos)
    file.close()
"""