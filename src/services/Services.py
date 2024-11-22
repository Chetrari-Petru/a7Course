class Services:
    def __init__(self, repository, student_class):
        self.storage = repository
        self.history = []
        self.student_class = student_class

    def add_student(self, args):
        new_student = self.student_class(args["name"], args["group"])
        self.storage.add_student(new_student)
        self.__write_history()

    def remove_student(self, args):
        _id = args["id"]

        index = -1
        the_list = self.storage.get_storage()

        for i in range(len(the_list)):
            if the_list[i].get_id() == _id:  # the_list[i] is a Student
                index = i
        if index == -1:
            print("Student is not added")
            return
        self.storage.remove_student(_id)
        self.__write_history()

    def filter(self, args):
        group_id = args["group"]

        indices = []

        the_list = self.storage.get_storage()
        for i in range(len(the_list)):
            if the_list[i].group == group_id:
                indices.append(i)

        self.storage.remove_students_by_indices(indices)
        self.__write_history()

    def __write_history(self):
        self.history.append(self.storage.get_storage())

    def undo(self):
        self.history.pop()
        self.storage.set_storage(self.history[-1])



        """
        storage = [2]
        history = [[1],
            [2]]
        """

