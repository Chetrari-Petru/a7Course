MemoryRepository:
    def __init__(self):
        self.__storage = [] # the list of students

    def get_storage(self):
        return self.__storage.copy()

    # add
    def add_student(self, student):
        self.__storage.append(student)

    # insert
    def insert_student(self, student, index):
        self.__storage.insert(index, student)

    # remove
    def remove_student(self, index):
        student = self.__storage.pop(index)
        student.remove()

    def remove_students_by_indices(self, indexes: list):
        storage_copy = []
        for i in indexes:
            self.__storage[i].remove()


        for index in range(len(self.__storage)):
            if not index in indexes:
                storage_copy.append(self.__storage[index])

        self.__storage = storage_copy
