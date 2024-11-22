import ui.UI as ui_class
from repository.Repository import RepositoryController
from domain.Student import Student
from services.Services import Services
from random import choice, randint


ui = ui_class.UI()
storage = RepositoryController(Student, "mem")
try:
    storage.import_repository()
except FileNotFoundError as e:
    print("Nothing to import")
service_engine = Services(storage, Student)


names = [
    "James", "Emma", "Michael", "Olivia", "William", "Sophia", "Alexander", "Isabella",
    "Benjamin", "Ava", "Jacob", "Mia", "Ethan", "Amelia", "Lucas", "Harper", "Mason",
    "Evelyn", "Henry", "Abigail", "Elijah", "Emily", "Daniel", "Ella", "Matthew",
    "Grace", "Samuel", "Lily", "Logan", "Scarlett"
]

for i in range(10):
    new_stud = {"name": choice(names), "group": randint(1, 3)}
    service_engine.add_student(new_stud)

while True:
    try:
        option, args = ui.run_step()
    except Exception as e:
        print(e)
        continue
    option = int(option)

    print()

    if option == 0:
        storage.write_repository()
        break

    if option == 1:
        service_engine.add_student(args)


    if option == 2:
        ui.pretty_print(storage.get_storage())



    if option == 3:
        service_engine.remove_student(args)

    if option == 4:
        service_engine.filter(args)

    if option == 5:
        service_engine.undo()

    if option == 6:
        try:
            storage.change_repository(args["new_repo"])
        except KeyError as Ke:
            print("Not a valid repository mode")