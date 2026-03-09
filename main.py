from voitures import Voitures
from parc import Parc
mon_parc = Parc(3)
voiture1 = Voitures("Toyota", "Corolla", "ABC13")
voiture2 = Voitures("Honda", "Civic", "XYZ789")
voiture3 = Voitures("kia", "Focus", "LMN456")
voiture4 = Voitures("Tesla", "Model 3", "TES123")
mon_parc.sortirVoiture(voiture2)
print("Places libres :", mon_parc.calculerNbrPlacesLibres())
print("Places libres après entrée des voitures :", mon_parc.calculerNbrPlacesLibres())
# Programme principal pour gérer le parc de voitures
