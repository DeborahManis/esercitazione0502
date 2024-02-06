# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import gaussian_kde

#importo il file
datiClima = pd.read_csv(r'C:\Users\Debor\OneDrive\Desktop\dataset_climatico.csv')
print(datiClima.head(10))#controllo i dati 

#pulizia dati
datiClima.dropna(inplace=True)  # Rimozione di valori mancanti

# Seleziona le colonne da standardizzare
colonne_da_normalizzare = ['temperatura_media', 'precipitazioni', 'umidita', 'velocita_vento']

# Calcololiamo la media e la deviazione standard 
medie = datiClima[colonne_da_normalizzare].mean()
deviazioni_standard = datiClima[colonne_da_normalizzare].std()

# Standardizzazione Z-score
datiClima[colonne_da_normalizzare] = (datiClima[colonne_da_normalizzare] - medie) / deviazioni_standard

print(datiClima.head(5))
#Analisi statistiche 
descrizione = datiClima.describe()
print(descrizione)
ColonneNorm = datiClima[colonne_da_normalizzare]
print(ColonneNorm.head(2))

# Crea grafici
for colonna in colonne_da_normalizzare:
 # Istogramma
    plt.hist(datiClima[colonna], bins=50, color='g', alpha=1)
    plt.title(f'Istogramma di {colonna}')
    plt.xlabel(colonna)
    plt.ylabel('Frequenza')
    plt.show()
 # Calcola la matrice di correlazione
#matrice_correlazione = datiClima[colonne_da_normalizzare].corr()

# Crea una heatmap con seaborn
# sns.heatmap(matrice_correlazione, annot=True, cmap='coolwarm', linewidths=.5)
# plt.title('Heatmap della Correlazione tra Variabili Meteorologiche')
# plt.show()
pd.plotting.scatter_matrix(datiClima[colonne_da_normalizzare],
                           diagonal="kde", alpha=0.5) 
plt.show()
