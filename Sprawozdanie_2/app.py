class App:

    def __init__(self):
        self.todo_list = []

    def display_menu(self):
        print("TODO List")
        print("==================")
        print("[1] Sprawdz liste")
        print("[2] Dodaj element do listy")
        print("[3] Zmodyfikuj element z listy")
        print("[4] Usun element z listy")
        print("[0] Wyjdz z programu")

        choice = input()
        if choice == "1":
            self.display_list()
        elif choice == "2":
            self.manage_list("0")
        elif choice == "3":
            self.manage_list("1")
        elif choice == "4":
            self.manage_list("2")
        elif choice == "0":
            return False
        else:
            self.display_error("invalid_choice")

        return True

    def display_list(self):
        if len(self.todo_list) == 0:
            self.display_error("empty_list")
        else:
            for i in range(len(self.todo_list)):
                print("Task {}: {}".format(i + 1, self.todo_list[i]))

    def insert_task(self):
        print("Co musisz zrobic?:")

        task = input() or False
        if not task:
            self.display_error("invalid_value")
        return task

    def insert_index(self):
        print("Wprowadz numer elementu listy:")

        index = int(input()) or False
        if not index:
            self.display_error("invalid_value")
        elif index > len(self.todo_list):
            index = False
            self.display_error("invalid_value")
        return index

    def manage_list(self, option):
        if option == '0':  # Add element
            task = self.insert_task()
            if task:
                self.todo_list.append(task)

        elif option == '1':  # Edit element
            index = self.insert_index()
            if index:
                task = self.insert_task()
                if task:
                    self.todo_list[index-1] = task

        elif option == '2':  # Delete element
            index = self.insert_index()
            if index:
                task = self.todo_list[index-1]
                if task:
                    self.todo_list.remove(task)

    @staticmethod
    def display_error(error_type):
        if error_type == "invalid_choice":
            print("Niepoprawny wybor! Sprobuj ponownie...")
        elif error_type == "invalid_value":
            print("Niepoprawna wartosc! Sprobuj ponownie...")
        elif error_type == "empty_list":
            print("Nie ma nic do wyswietlenia! Lista jest pusta.")

        print("==================")


def main():
    app = App()
    is_on = True

    while is_on:
        is_on = app.display_menu()


if __name__ == "__main__":
    main()
