class Person:
    kind = "vocaloid"

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)


person = Person("Miku", 16)
print(person.name, person.age, person.kind, person.songs)

person.add_song("ヴァンパイア")
person.add_song("シンデレラ")
print(person.name, person.age, person.kind, person.songs)
