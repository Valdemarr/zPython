#FCC objects with our good friend Dr. Chuck Severance

class PartyAnimal:
    count = 0

    def party(self):
        self.count += 1
        print("So far", self.count)
    
an = PartyAnimal()

# an.party() == PartyAnimal.party(an)
an.party()
PartyAnimal.party(an)
an.party()
