



class UI:
    def __init__(self):
        self.__options = {
            "0": {"description": "Exit the application", "function": self.__exit},

            "1": {"description": "Add a student", "function": self.__add_student},
            "2": {"description": "List students", "function": self.__none_function},
            "3": {"description": "Delete a student", "function":self.__delete_student},
            "4": {"description": "Filter students", "function":self.__filter_by_group},
            "5": {"description": "Undo the last operation", "function":None},
        }

    def __none_function(self):
        # this function does nothing
        return

    def __exit(self):
        return "exit"

    def __add_student(self):
        name = input("Enter student name: ")
        group = input("Enter group number: ")

        if group == "":
            group = None
        if not group is None:
            group = int(group)



        return {"name": name, "group": group}

    def __delete_student(self):
        id = input("Enter student id: ")
        id = int(id)
        return {"id": id}

    def __filter_by_group(self):
        group = input("Enter group number: ")
        group = int(group)
        return {"group": group}



    def __print_menu(self):
        for key in self.__options:
            print(key, " ", self.__options[key]["description"])

        print()

    def run_step(self):
        self.__print_menu()
        option = input()

        result = self.__options[option]["function"]()
        if result == "exit":
            print("Exiting the program")
            return 0

        return option, result