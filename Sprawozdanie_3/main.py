import requests
from bs4 import BeautifulSoup


class App:
    def __init__(self, website):
        self.website = website
        self.result = requests.get(website)
        self.src = self.result.content
        self.soup = BeautifulSoup(self.src, 'lxml')
        self.link_list = []

    def get_links(self):
        links = self.soup.find_all("a")
        return links

    def add_elements_to_list(self):
        links = self.get_links()
        for link in links:
            if link.get('href') is not None:
                if link.get('href').startswith("/"):
                    element = self.website + link.get('href')
                else:
                    element = link.get('href')
                self.link_list.append(element)

    def display_link_list(self):
        if not self.link_list:
            print("Lista linkow jest pusta!")
        else:
            for link in self.link_list:
                print(link)


def is_accessable(website):
    result = requests.get(website)
    if result.status_code == 200:
        return True
    else:
        return False


def main():
    print('Podaj adres strony z ktorej chcesz pobrac dane ("https://www.google.com"):')
    website = input()
    if is_accessable(website):
        app = App(website)
        app.add_elements_to_list()
        print("Lista linkow:")
        app.display_link_list()
    else:
        print("Nie mozna pobrac zawartosci danej witryny.")


if __name__ == '__main__':
    main()
