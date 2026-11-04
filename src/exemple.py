def calculer_moyenne(notes):
    total = 0
    for note in notes:
        total += note
    return total / len(notes)


notes_etudiants = [15, 12, 18, 9, 14]
moyenne = calculer_moyenne(notes_etudiants)
print(f"La moyenne des notes est : {moyenne}")