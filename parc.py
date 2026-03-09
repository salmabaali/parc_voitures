class Parc:
    def __init__(self, capacite):
        self.capacite = capacite
        self.voitures = []

    def entrerVoiture(self, voiture):
        if voiture in self.voitures:
            print("La voiture est déjà dans le parc")
        elif len(self.voitures) >= self.capacite:
            print("Le parc est plein")
        else:
            self.voitures.append(voiture)
            print(f"Voiture {voiture.marque} {voiture.modele} entrée dans le parc.")

    def sortirVoiture(self, voiture):
        if voiture not in self.voitures:
            print("La voiture n'est pas dans le parc")
        else:
            self.voitures.remove(voiture)
            print(f"Voiture {voiture.marque} {voiture.modele} sortie du parc.")

    def calculerNbrPlacesLibres(self):
        return self.capacite - len(self.voitures)
    