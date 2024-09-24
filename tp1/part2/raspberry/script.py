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

    plt.title('Consommation de la puissance de ' + filename.split('-')[1] + filename.split('-')[2])
    plt.xlabel('Temps (s)')
    plt.ylabel('Puissance (W)')

    beg = list(data.keys())[0]

    plt.plot([v - beg for v in data.keys()], data.values())

    plt.legend()
    plt.grid(True)
    plt.show()

def power_avg_comparison_graph(bench1_avg: float, bench2_avg: float, bench3_avg: float):
    plt.figure(figsize=(10, 6))

    plt.title('Comparaison de la puissance moyenne')
    plt.ylabel('Puissance (W)')
    
    plt.bar(('bench3', 'bench2', 'bench1'), (bench3_avg, bench2_avg, bench1_avg), color=('green', 'blue', 'gray'))

    plt.show()

idle_file = 'idle.csv'  
bench1_files = ['rpi-bench-11.csv']
bench2_files = ['rpi-bench-12.csv']
bench3_files = ['rpi-bench-13.csv']

idle_avg = compute_avg(idle_file)

bench1_avg = sum([compute_avg(file) for file in bench1_files]) / len(bench1_files)
bench2_avg = sum([compute_avg(file) for file in bench2_files]) / len(bench2_files)
bench3_avg = sum([compute_avg(file) for file in bench3_files]) / len(bench3_files)


print(f'Consommation moyenne en IDLE : {idle_avg:.2f} W')
print(f'Consommation moyenne du bench 1 : {bench1_avg:.2f} W')
print(f'Consommation moyenne du bench 2 : {bench2_avg:.2f} W')
print(f'Consommation moyenne du bench 3 : {bench3_avg:.2f} W')


bench1_avg -= idle_avg
bench2_avg -= idle_avg
bench3_avg -= idle_avg

power_evolution_graph(bench1_files[0])
power_evolution_graph(bench2_files[0])
power_evolution_graph(bench3_files[0])

power_avg_comparison_graph(bench1_avg, bench2_avg, bench3_avg)
