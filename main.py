# Alec Martin 2152076, 06/10/2022
# Exercice 4.3 Pourboire

# Si la facture est en bas d'un certain montant (10$), un montant fixe est utilisé (1.50$).
# Ensuite, jusqu'à 100$, on calcule simplement 15%. À partir de 100$, un montant de
# départ est fixé à 15$ et on ajoute 5%. Pour une facture à partir de 200$ le
# pourboire est inclus.

# On affiche la facture
# • prix total incluant le pourboire et
# • la valeur du pourboire avec la mention que c'est inclus dans le prix total.

# LIMITES DU PROGRAMME : Il faut que l'utilisateur input un chiffre

from typing import Final
import locale

locale.setlocale(locale.LC_ALL, '')  # Set l'argent à la monnaie locale de l'utilisateur


# CONSTANTES ET VARIABLES

class ValeursLimites:  # Les valeurs où la fonction pour calculer le pourboire change
    POUR_MONTANT_FIXE = 10  # En bas de 10$, on paye 1.50$ de pourboire
    POUR_POURCENTAGE = 100  # Entre 10$ et 100$, on paye 15% de plus en pourboire
    POUR_LINEAIRE = 200  # Entre 100 et 200$, c'est une fonction linéaire
    # En haut de 200$, il n'y a pas de pourboire à donner


prixAvantPourboire: float  # Prix de l'achat
coutTotal: float  # Prix avec pourboire

MONTANT_FIXE: Final = 1.5  # Lorsque le prix est en bas de 10$
TAUX_A_PAYER: Final = 0.15  # Lorsque le prix est entre 10 et 100$
MONTANT_FIXE_DE_FONCTION: Final = 15  # Lorsque le prix est entre 100 et 200$
TAUX_DE_FONCTION: Final = 0.05  # Lorsque le prix est entre 100 et 200$

# LOGIQUE

print('Quel est le prix total de l\'achat?')
prixAvantPourboire = float(input(''))

if 0 < prixAvantPourboire < 10:
    coutTotal = prixAvantPourboire + MONTANT_FIXE
elif 10 <= prixAvantPourboire < 100:
    coutTotal = prixAvantPourboire + (prixAvantPourboire * TAUX_A_PAYER)
elif 100 <= prixAvantPourboire < 200:
    coutTotal = prixAvantPourboire + (prixAvantPourboire * TAUX_DE_FONCTION) + MONTANT_FIXE_DE_FONCTION
elif 200 <= prixAvantPourboire:
    coutTotal = prixAvantPourboire
else:
    print('wtf')

print('Le coût total est de {:.2f} $, ce qui inclue le pourboire de'.format(coutTotal),
      locale.currency(coutTotal-prixAvantPourboire))

# J'ai mis un {:.2f} pour montrer que je sais comment faire mais je préfère locale.currency
