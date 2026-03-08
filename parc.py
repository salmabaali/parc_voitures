class Parc:
    def __init__(self, capacite):
        self.capacite = capacite
        self.voitures = []

    def entrerVoiture(self, voiture):
        if voiture in self.voitures:
            print("La voiture est deja dans le parc")
        elif len(self.voitures) >= self.capacite:
            print("Le parc est plein")
        else:
            self.voitures.append(voiture)
            print("Voiture ajoutee au parc")