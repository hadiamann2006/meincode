noten=[]

while True:
    note = float(input("Note hinzufügen: "))
    noten.append(note)

    # durchschnitt berechnen
    summe = 0
    n = len(noten)
    for note in noten:
        summe = summe + note
    durchschnitt = summe / n

    print("------------------------")
    print("Noten: " + str(noten))
    print("Durchschnitt: " + str(durchschnitt))
    print("------------------------")
    

# Notendurchschnittsberechner
## Einleitung: Mit diesem Program kann man den persönlichen Notendurchschnitt berechnen. Dabei müssen Sie ihre gesamten Noten angeben. Sofort wird Ihnen ihr momentaner Notendurchschnitt angegeben.
    

