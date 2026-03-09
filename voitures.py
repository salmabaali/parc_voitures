class Voiture:
    def __init__(self, marque, modele, immatriculation):
        self.marque = marque
        self.modele = modele
        self.immatriculation = immatriculation

    def __eq__(self, autre):
        return isinstance(autre, Voiture) and self.immatriculation == autre.immatriculation

    def __hash__(self):
        return hash(self.immatriculation)
