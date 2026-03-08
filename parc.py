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
    def sortirVoiture(self, voiture):
        if voiture in self.voitures:
            self.voitures.remove(voiture)
            print("Voiture retiree du parc")
        else:
            print("La voiture n'est pas dans le parc")