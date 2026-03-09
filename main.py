from voitures import Voiture
from parc import Parc
mon_parc = Parc(capacite=3)

# Créer les voitures
voiture1 = Voiture("Toyota", "Corolla", "ABC13")
voiture2 = Voiture("Honda", "Civic", "DEF45")
voiture3 = Voiture("Kia", "Focus", "LMN456")

# Entrer les voitures dans le parc
mon_parc.entrerVoiture(voiture1)
mon_parc.entrerVoiture(voiture2)
mon_parc.entrerVoiture(voiture3)

# Afficher les places libres
print("Places libres après entrée des voitures :", mon_parc.calculerNbrPlacesLibres())

mon_parc.sortirVoiture(voiture2)

# Afficher les places libres après sortie
print("Places libres après sortie d'une voiture :", mon_parc.calculerNbrPlacesLibres())

