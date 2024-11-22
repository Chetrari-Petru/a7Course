import ui.UI as ui_class
from repository.Repository import MemoryRepository
from domain.Student import Student


ui = ui_class.UI()

storage = MemoryRepository()

while True:
    try:
        option, args = ui.run_step()
    except Exception as e:
        print(e)
        continue
    option = int(option)

    print()

    if option == 0:
        break

    if option == 1:
        new_student = Student(args["name"], args["group"])
        storage.add_student(new_student)


    if option == 2:
        print(storage.get_storage())



    if option == 3:
        _id = args["id"]


        index = -1
        the_list = storage.get_storage()

        for i in range(len(the_list)) :
            if the_list[i].get_id() == _id: # the_list[i] is a Student
                index = i
        if index == -1:
            print("Student is not added")
            continue
        storage.remove_student(_id)

    if option == 4:
        group_id = args["group"]

        indices = []

        the_list = storage.get_storage()
        for i in range(len(the_list)) :
            if the_list[i].group == group_id:
                indices.append(i)

        storage.remove_students_by_indices(indices)
