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

    plt.title('Consommation de la puissance de ' + filename.split('-')[0])
    plt.xlabel('Temps (s)')
    plt.ylabel('Puissance (W)')

    beg = list(data.keys())[0]

    plt.plot([v - beg for v in data.keys()], data.values())

    plt.legend()
    plt.grid(True)
    plt.show()

def power_avg_comparison_graph(firefox_avg: float, chrome_avg: float):
    plt.figure(figsize=(10, 6))

    plt.title('Comparaison de la puissance moyenne')
    plt.ylabel('Puissance (W)')
    
    plt.bar(('Chrome', 'Firefox'), (chrome_avg, firefox_avg), color=('green', 'blue'))

    plt.show()

idle_file = 'idle.csv'  
firefox_files = ['firefox-1.csv', 'firefox-2.csv', 'firefox-3.csv']
chrome_files = ['chrome-1.csv', 'chrome-2.csv', 'chrome-3.csv']

idle_avg = compute_avg(idle_file)
firefox_avg = sum([compute_avg(file) for file in firefox_files]) / len(firefox_files)
chrome_avg = sum([compute_avg(file) for file in chrome_files]) / len(chrome_files)

print(f'Consommation moyenne en IDLE : {idle_avg:.2f} W')
print(f'Consommation moyenne de Chrome : {chrome_avg:.2f} W')
print(f'Consommation moyenne de Firefox : {firefox_avg:.2f} W')


firefox_avg -= idle_avg
chrome_avg -= idle_avg

power_evolution_graph(firefox_files[0])
power_evolution_graph(chrome_files[0])

power_avg_comparison_graph(firefox_avg, chrome_avg)
