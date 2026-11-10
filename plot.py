import csv
import numpy as np
import matplotlib.pyplot as plt

file_path = "C:/Users/macie/Downloads/gjennomsnittlig-rslnn.csv"
data_liste = []

with open(file_path, "r", encoding="utf-8-sig") as file:
    leser = csv.reader(file, delimiter=";")
    next(leser)  # Hopper over overskriften
    for line in leser:
        aar = int(line[0])
        lonn = int(line[1].replace("\xa0", "").replace(" ", ""))
        data_liste.append([aar, lonn])

data_array = np.array(data_liste)

# 1. Hent ut aksene fra NumPy-arrayen
aar = data_array[:, 0]
lonn = data_array[:, 1]

# 2. Opprett plottet
plt.figure(figsize=(8, 5))
plt.plot(aar, lonn, marker="o", color="b", linestyle="-", linewidth=2)

# 3. Legg til tittel, aksetekster og rutenett
plt.title("Gjennomsnittlig årslønn (2018–2025)")
plt.xlabel("År")
plt.ylabel("Årslønn (NOK)")
plt.grid(True)

# 4. Viss bildet på skjermen
plt.show()