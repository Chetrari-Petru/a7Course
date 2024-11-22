class IdGenerator:
    def __init__(self):
        self.__last_id = 0
        self.__unused_ids = []

    def gen_id(self):
        if len(self.__unused_ids) == 0:
            chosen_id =  self.__last_id
            self.__last_id += 1
            return chosen_id

        return self.__unused_ids.pop()

    def remove_id(self, chosen_id):
        self.__unused_ids.append(chosen_id)