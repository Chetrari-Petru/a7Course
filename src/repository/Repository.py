import os
import pickle

repo_modes = ["file", "memory", "binary"]

class RepositoryController:
    def __init__(self, student_class, mode = "default"):
        self.modes = {
            "default": repo_modes[1],

            "f": repo_modes[0],
            "file": repo_modes[0],
            "memory": repo_modes[1],
            "mem": repo_modes[1],
            "binary": repo_modes[2],
            "b": repo_modes[2]
        }


        self.mem_repo = MemoryRepository()
        self.working_path = os.getcwd()+"\\"
        self.file_repo = TextFileRepository(student_class)
        self.binary_repo = BinaryFileRepository(student_class)
        self.current_mode = self.modes[mode]

        self.additional_repos= {repo_modes[0]: self.file_repo, repo_modes[2]: self.binary_repo}

    def get_storage(self):
        return self.mem_repo.get_storage()

    def set_storage(self, storage):
        self.mem_repo.set_storage(storage)

    def add_student(self, student):
        self.mem_repo.add_student(student)

    def insert_student(self, student, index):
        self.mem_repo.insert_student(student, index)

    def remove_student(self, index):
        self.mem_repo.remove_student(index)

    def remove_students_by_indices(self, indexes: list):
        self.mem_repo.remove_students_by_indices(indexes)

    def write_repository(self):
        if self.current_mode == repo_modes[1]:
            return

        self.additional_repos[self.current_mode].write_repository(self.mem_repo.get_storage(),
                                                                  self.working_path)

    def import_repository(self):
        if self.current_mode == repo_modes[1]:
            return

        storage = self.additional_repos[self.current_mode].import_repository(self.working_path)
        self.mem_repo.set_storage(storage)

    def change_repository(self, new_repository):
        if not new_repository in self.modes.keys():
            raise KeyError("Invalid repository")
        self.write_repository()
        self.current_mode = self.modes[new_repository]
        self.import_repository()

class MemoryRepository:
    def __init__(self):
        self.__storage = [] # the list of students

    def get_storage(self):
        return self.__storage.copy()

    def set_storage(self, storage):
        self.__storage = storage

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


class TextFileRepository:
    """
    file_format -> Computer_compatible_format
    Computer_compatible_format -> file format

    students are separated by newlines
    <int: id>, <str:name>, <int: group>

    5, ALex, 4
    """
    def __init__(self, student_class):
        self.__student_class = student_class

    def import_repository(self, file_path):
        with open(file_path+"Storage.repo", 'r') as f:
            imported_storage = []
            try:
                while True:
                    line = f.readline()
                    args = line.split(",")
                    args[-1] = args[-1].strip()
                    if line == "":
                        break

                    # _id = int(args[0])
                    name = args[1]
                    group = int(args[2])

                    new_student = self.__student_class(name, group)
                    imported_storage.append(new_student)


            except ValueError:
                print("ValueError")
                return IOError("File format not good. it bad")
            return imported_storage

    def write_repository(self, storage, storage_path):
        with open(storage_path+"Storage.repo", 'w') as f:
            file_content = ""
            for student in storage:
                student_entry =str(student.get_id())+","+student.name+","+str(student.group)
                file_content = file_content+student_entry+"\n"
            f.write(file_content)


class BinaryFileRepository:
    def __init__(self, student_class):
        self.__student_class = student_class

    def import_repository(self, file_path):
        with open(file_path + "Storage.pik", 'rb') as f:
            try:
                imported_storage = pickle.load(f)


            except ValueError:
                print("ValueError")
                return IOError("File format not good. it bad")
            return imported_storage

    def write_repository(self, storage, storage_path):
        file = open(storage_path+"Storage.pik", 'wb')
        pickle.dump(storage, file)
        file.close()



