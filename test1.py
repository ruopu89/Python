from test2 import Person
from test3 import get_score

def monkeypatch4Person():
    Person.get_score = get_score

monkeypatch4Person()

if __name__ == "__main__":
    print(Person().get_score())