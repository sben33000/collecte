def calculer_moyenne(nombres):
    """Retourne la moyenne d'une liste de nombres."""
    if not nombres:
        raise ValueError("La liste est vide, impossible de calculer une moyenne.")
    return sum(nombres) / len(nombres)


if __name__ == "__main__":
    saisie = input("Entrez des nombres séparés par des espaces : ")
    try:
        nombres = [float(n.replace(",", ".")) for n in saisie.split()]
        print(f"Moyenne : {calculer_moyenne(nombres):.2f}")
    except ValueError as erreur:
        print(f"Erreur : {erreur}")