# without class

def example_tuple():
    t01 = "John", "White", 24
    print(t01)
    print(t01[1])

def example_dict():
    d02 = {"first_name": "John", "last_name": "White", "age": 24}
    print(d02)
    print(d02["last_name"])

"""______________________________________"""

class Player_01:
    pass

class Player_02:
    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.age = 0

class Player_03:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

def example_class_player_01():
    c01 = Player_01()
    c01.first_name = "John"
    c01.last_name = "White"
    c01.age = 24
    print(c01.last_name)

def example_class_player_02():
    c02 = Player_02()
    c02.first_name = "John"
    c02.last_name = "White"
    c02.age = 24
    print(c02.last_name)

def example_class_player_03():
    c03 = Player_03("John", "White", 24)
    print(c03.last_name)

if __name__ == "__main__":
    # without class
    example_tuple()
    example_dict()

    # with class
    example_class_player_01()
    example_class_player_02()
    example_class_player_03()