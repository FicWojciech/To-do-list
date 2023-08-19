to_do_list = []


while True:

    def adding_todo():
        to_do_list.append(input("Wpisz zadanie: "))
        print(f"Pomyślnie dodano {to_do_list}!")

    def see_things():
        print(to_do_list)

    def remove_item():
        to_do_list.remove(input("Co chcesz usunac? "))
        print("Pomyślnie usunięto.")

    def clear_list():
        print("Czy na pewno chcesz wyczyścić listę?")
        clear_choice = input("Y or N ")
        if clear_choice == "Y" or clear_choice == "y":
            to_do_list.clear()
        elif clear_choice == "N" or clear_choice == "n":

            def see_things():
                print(to_do_list)

    def create_file():
        print("Chcesz stworzyć plik txt?")
        answer = input("Y or N ")
        if answer == "Y" or answer == "y":
            inputFile = "ToDoList.txt"
        with open(inputFile, "w") as filedata:
            for item in to_do_list:
                filedata.write("%s\n" % item)
            filedata.close()

    def open_file():
        fileData = open("ToDoList.txt")
        print(fileData.read())

    print("Dostępne opcje:")
    print("Kliknij 1 żeby dodać nową rzecz do zrobienia")
    print("Kliknij 2 żeby zobaczyć rzeczy do zrobienia")
    print("Kliknij 3 żeby usunąć rzecz")
    print("Kliknij 4 żeby wyczyścić liste")
    print("Kliknij 5 żeby stworzyć plik txt")
    print("Kliknij 6 żeby odczytać stworzony plik")
    print("Kliknij 7 żeby zakończyć")
    choice = input("Co chcesz zrobić? ")

    if choice == "1":
        adding_todo()
    elif choice == "2":
        see_things()
    elif choice == "3":
        remove_item()
    elif choice == "4":
        clear_list()
    elif choice == "5":
        create_file()
    elif choice == "6":
        open_file()
    else:
        print("Dziękuję za skorzystanie.")
        break
