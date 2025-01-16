class Auto:
    def __init__(self, ps):
        if not isinstance (ps, (int, float)) or ps < 0:
            raise ValueError("Keine Zahl angegeben!!!")
        self.ps = ps
    
    def __add__(self, fahrzeug):
        if not isinstance(fahrzeug, Auto):
            raise ValueError("Es können nur Autos addiert werden!!")
        return Auto(self.ps + fahrzeug.ps)
    
    def __sub__(self, fahrzeug):
        if not isinstance(fahrzeug, Auto):
            raise ValueError("Es können nur Autos subtrahiert werden!!")
        return Auto(self.ps - fahrzeug.ps)
    
    def __mul__(self, fahrzeug):
        if not isinstance(fahrzeug, Auto):
            raise ValueError("Es können nur Autos multipliziert werden!!")
        return Auto(self.ps * fahrzeug.ps)

    def __eq__(self, fahrzeug):
        if not isinstance(fahrzeug, Auto):
            raise ValueError("Es können nur Autos verglichen werden!!")
        return self.ps == fahrzeug.ps

    def __lt__(self, fahrzeug):
        if not isinstance(fahrzeug, Auto):
            raise ValueError("Es können nur Autos verglichen werden!!")
        return self.ps < fahrzeug.ps

    def __gt__(self, fahrzeug):
        if not isinstance(fahrzeug, Auto):
            raise ValueError("Es können nur Autos verglichen werden!!")
        return self.ps > fahrzeug.ps

    def __len__(self):
        return self.ps

    def __repr__(self):
        return f"Auto({self.ps} PS)"

def main():
    a1 = Auto(50)
    a2 = Auto(60)

    print(a1 + a2)

    print(a2 - a1)

    print(a1 * a2)

    print(a1 == a2)
    print(a1 < a2)
    print(a1 > a2)

    print(len(a1))

    try:
        print(a1 + 5)
    except Exception as error:
        print(error)

    
    try:
        print(a1 - "Test")
    except Exception as error:
        print(error)

    try:
        print(a1 * a2)
    except Exception as error:
        print(error)

    


if __name__ == "__main__":
    main()