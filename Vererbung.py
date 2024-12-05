class Genre:
    def __init__(self, genre):
        self.genre = genre
    
    def __str__(self):
        return f"{self.genre}"
    

class Spiele(Genre):
    def __init__(self, name, jahr, firma, genre):
        self.name = name
        self.jahr = jahr
        self.firma = firma
        super().__init__(genre)
    
    def __str__(self):
        return f"{self.name}({self.jahr}) von {self.firma} ist ein {super().__str__()}"
    

Tekken8 = Spiele("Tekken 8", 2024, "Bandai Namco", "Fighting Game")
print(Tekken8)

SF6 = Spiele("Street Fighter 6", 2023, "Capcom", "Fighting Game")
print(SF6)

BO3 = Spiele("Call of Duty - Black Ops 3", 2015, "Activision", "Shooter")
print(BO3)