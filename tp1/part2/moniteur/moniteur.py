import matplotlib.pyplot as plt
import csv

def parse_csv(filename: str):
    data = {}

    with open(filename) as file:
        csvfile = csv.reader(file, delimiter=';')
        for timestamp, value in csvfile:
            if timestamp == 'Timestamp':
                continue

            data[int(timestamp)] = float(value)

    return data

def compute_avg(filename: str):
        data = parse_csv(filename)

        return sum(data.values()) / len(data.values())

def power_evolution_graph(filename: str):
    data = parse_csv(filename)

    plt.figure(figsize=(10, 6))

    plt.title('Consommation de la puissance du moniteur avec une luminosité de ' + filename.replace('.csv', '').split('ecran')[1] + '%')
    plt.xlabel('Temps (s)')
    plt.ylabel('Puissance (W)')

    beg = list(data.keys())[0]

    plt.plot([v - beg for v in data.keys()], data.values())

    plt.legend()
    plt.grid(True)
    plt.show()

bench10_files = ['ecran10.csv']
bench30_files = ['ecran30.csv']
bench50_files = ['ecran50.csv']
bench100_files = ['ecran100.csv']


bench10_avg = sum([compute_avg(file) for file in bench10_files]) / len(bench10_files)
bench30_avg = sum([compute_avg(file) for file in bench30_files]) / len(bench30_files)
bench50_avg = sum([compute_avg(file) for file in bench50_files]) / len(bench50_files)
bench100_avg = sum([compute_avg(file) for file in bench100_files]) / len(bench100_files)


print(f'Consommation moyenne avec la luminosité à 10% : {bench10_avg:.2f} W')
print(f'Consommation moyenne avec la luminosité à 30% : {bench30_avg:.2f} W')
print(f'Consommation moyenne avec la luminosité à 50% : {bench50_avg:.2f} W')
print(f'Consommation moyenne avec la luminosité à 100% : {bench100_avg:.2f} W')


power_evolution_graph(bench10_files[0])
power_evolution_graph(bench30_files[0])
power_evolution_graph(bench50_files[0])
power_evolution_graph(bench100_files[0])

