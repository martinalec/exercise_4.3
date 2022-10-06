# Alec Martin 2152076, 06/10/2022
# Exercice 4.3 Pourboire

# Si la facture est en bas d'un certain montant (10$), un montant fixe est utilisé (1.50$).
# Ensuite, jusqu'à 100$, on calcule simplement 15%. À partir de 100$, un montant de
# départ est fixé à 15$ et on ajoute 5%. Pour une facture à partir de 200$ le
# pourboire est inclus.

# On affiche la facture
# • prix total incluant le pourboire et
# • la valeur du pourboire avec la mention que c'est inclus dans le prix total.

# CONSTANTES ET VARIABLES

class ValeursLimites:  # Les valeurs où la fonction pour calculer le pourboire change
    POUR_MONTANT_FIXE: float = 10  # En bas de 10$, on paye 1.50$ de pourboire
    POUR_POURCENTAGE: float = 100  # Entre 10$ et 100$, on paye 15% de plus en pourboire
    POUR_LINEAIRE: float = 200  # Entre 100 et 200$, c'est une fonction linéaire
    # En haut de 200$, il n'y a pas de pourboire à donner


PRIX = float  # Prix de l'achat


montantFixe = 1.5  # Lorsque le prix est en bas de 10$
tauxAPayer = 0.15  # Lorsque le prix est entre 10 et 100$
fonctionLineaire = (0.5 * PRIX) + 15  # Lorsque le prix est entre 100 et 200$


# LOGIQUE
