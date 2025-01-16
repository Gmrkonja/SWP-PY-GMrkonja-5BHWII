class Genre:
    def __init__(self, bezeichnung):
        if not isinstance(bezeichnung, str):
            raise ValueError("Wurde kein bezeichnung gegeben!!")
        self.bezeichnung = bezeichnung
    
    def __str__(self):
        return f"{self.bezeichnung}"
    

class Spiele(Genre):
    def __init__(self, name, jahr, firma, bezeichnung):
        self.name = name
        self.jahr = jahr
        self.firma = firma
        super().__init__(bezeichnung)


    def __str__(self):
        return f"{self.name}({self.jahr}) von {self.firma} ist ein {super().__str__()}"


try:
    Shooter = Genre(12)
    print(Shooter)
except Exception as Error:
    print(Error)

try:
    Fighting = Genre("Fighting")
    print(Fighting)
except Exception as Error:
    print(Error)

Tekken8 = Spiele("Tekken 8", 2024, "Bandai Namco", "Fighting Game")
print(Tekken8)

SF6 = Spiele("Street Fighter 6", 2023, "Capcom", "Fighting Game")
print(SF6)

BO3 = Spiele("Call of Duty - Black Ops 3", 2015, "Activision", "Shooter")
print(BO3)