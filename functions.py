FILEPATH = "/Users/zeeshan/app1/GIT/todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of
    to-do items.
    :param filepath:
    :return:
    """

    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_args, filepath=FILEPATH):
    """ Write the to-do items list in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_args)


if __name__ == "__main__":
    print("Hello!")
    print(get_todos())


# def get_todos(filepath=FILEPATH):
#     """ Read a text file and return a list of
#     to-do items.
#     """
#     with open(filepath, 'r') as file_local:
#         todos_local = file_local.readlines()
#     return todos_local
#
#
# def write_todos(todos_args, filepath=FILEPATH):
#     """ write a to-do items list in a text file.
#
#     :param filepath:
#     :param todos_args:
#     :return:
#     """
#     with open(filepath, 'w') as file:
#         file.writelines(todos_args)
#
#
# if __name__ == "__main__":
#     print("Hello!")
#     print(get_todos())