import domain.IdGenerator as id_gen

id_gen = id_gen.IdGenerator()

class Student:
    # storage
    def __init__(self, name, group = 0):
        self.__id = id_gen.gen_id()
        self.name = name
        self.group = group
        if self.group is None:
            self.group = 0


    # functionalities
    def get_id(self):
        return self.__id

    def remove(self):
        id_gen.remove_id(self.__id)

    def __repr__(self):
        return "(id {0}, name {1}, group {2})".format(self.__id, self.name, self.group)
