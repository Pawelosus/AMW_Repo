import os


class App:
    def __init__(self, first_var, second_var, option):
        self.first_var = first_var
        self.second_var = second_var
        self.option = option

    def calculate(self):
        if self.option == '1':
            return self.first_var + self.second_var
        elif self.option == '2':
            return self.first_var - self.second_var
        elif self.option == '3':
            return self.first_var * self.second_var
        elif self.option == '4':
            return self.first_var / self.second_var


def main():
    on = True
    while on:
        print("Podaj pierwsza liczbe:")
        first_var = int(input())

        print("Podaj druga liczbe:")
        second_var = int(input())

        clear = os.system('cls')

        print("Co chcesz z nimi zrobic?")
        print("[1] Dodac")
        print("[2] Odjac")
        print("[3] Pomnozyc")
        print("[4] Podzielic")
        print("[0] Wyjsc :)")
        print("Wybor: ")

        option = input()

        if option == '1' or option == '2' or option == '3' or option == '4':
            app = App(first_var, second_var, option)
            print("Wynik: ", app.calculate())
        elif option == '0':
            on = False


if __name__ == "__main__":
    main()