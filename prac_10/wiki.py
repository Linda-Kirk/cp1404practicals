import wikipedia


def main():
    search_parameter = input("Enter page title or search phrase: ")
    while search_parameter != "":
        try:
            page = summary(search_parameter)
            print(page.title)
            print(page.summary)
            print(page.url)
        except wikipedia.exceptions.DisambiguationError as e:
            print(e.options)

        search_parameter = input("Enter page title or search phrase: ")


def summary(search_parameter):
    return wikipedia.page(search_parameter)


main()
