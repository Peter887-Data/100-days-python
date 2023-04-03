gericht = input("Wähle ein Gericht? ")

def ausgabe_italien():
  print("Italien")

def ausgabe_russland():
  anzahl_pieroggen = 37
  print(f"Russland {anzahl_pieroggen}")

def ausgabe_deutschland():
  print("Deutschland")


# Ausgabe mit if/else
if gericht == "Spaghetti":
  ausgabe_italien()
elif gericht == "Pieroggen":
  ausgabe_russland()
elif gericht == "Sauerkraut":
  ausgabe_deutschland()
else:
  print("Keine Ahnung!")


# Ausgabe mit dict
gericht_zu_land = {
  "Spaghetti": ausgabe_italien,
  "Pieroggen": ausgabe_russland,
  "Sauerkraut": ausgabe_deutschland
}

land = gericht_zu_land.get(gericht)

if land != None:
  land()
else:
  print("Keine Ahnung!")
