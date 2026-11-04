def mediane(valeurs):
    valeurs = sorted(valeurs)
    n = len(valeurs)
    milieu = n // 2
    if n % 2 == 1:
        return valeurs[milieu]
    return (valeurs[milieu - 1] + valeurs[milieu]) / 2