from collections import namedtuple

class Persons:
    def __init__(self, persons):
        try:
            self._persons = [person.first.capitalize() + ' ' + person.last.capitalize()
                             for person in persons]
        except (TypeError) or (AttributeError):
            self._persons = []
    
    def __iter__(self):
        return iter(self._persons)

if __name__ == '__main__':

    Person = namedtuple('Person', 'first last')

    persons = [Person('kirAn', 'ramachandran'), Person('nirVan', 'kiran'), Person('Namita', 'nair')]

    person_names = Persons(persons)

    for name in person_names:
        print(name)
