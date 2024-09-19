import pandas as pd
import matplotlib.pyplot as plt

def calculate_and_plot_power_statistics(csv_file):
    # Chargement des données CSV
    data = pd.read_csv(csv_file, delimiter=';')
    
    # Affichage des premières lignes pour vérifier les données
    print("Aperçu des premières lignes du fichier CSV :")
    print(data.head(), "\n")
    
    # Calcul des statistiques : moyenne, écart-type
    mean_power = data['Power'].mean()
    std_dev = data['Power'].std()

    # Affichage des résultats des calculs
    print(f"Puissance moyenne : {mean_power} W")
    print(f"Écart-type : {std_dev} W\n")

    # Ajustement des timestamps (pour commencer à 0)
    data['Timestamp'] = data['Timestamp'] - data['Timestamp'].min()
    
    # Génération du graphique
    plt.figure(figsize=(10, 6))
    plt.plot(data['Timestamp'], data['Power'], color='blue', marker='o', linestyle='-', markersize=4)
    
    # Titres et légendes
    plt.title("Évolution de la puissance en fonction du temps")
    plt.xlabel("Temps (s)")
    plt.ylabel("Puissance (W)")
    
    # Ajout d'une grille
    plt.grid(True)
    
    # Affichage du graphique
    plt.show()

# Utilisation de la fonction
csv_file = 'idle.csv'  # Chemin vers le fichier CSV
calculate_and_plot_power_statistics(csv_file)
