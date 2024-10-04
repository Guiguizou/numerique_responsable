import subprocess
import time
from datetime import datetime, timedelta

pause_duration = 10
runtime = 30

def compile_programs():
    print("Compilation des programmes")

    print("Compilation du programme C")
    subprocess.run("gcc -o ray_casting ray_casting.c -std=c99 -lm", shell=True, check=True)

    print("Compilation du programme Java original")
    subprocess.run("javac RayCasting.java", shell=True, check=True)

    print("Compilation du programme Java modifié")
    subprocess.run("javac RayCastingAlternative.java", shell=True, check=True)

    print("Tous les programmes ont été compilés\n")

def run_program_for_duration(command, duration, log_file):
    start_time = datetime.now()
    print(f"Démarrage de {command} à {start_time.strftime('%H:%M:%S')}")
    
    with open(log_file, 'a') as log:
        log.write(f"Démarrage de {command} à {start_time.strftime('%H:%M:%S')}\n")
    
    end_time = start_time + timedelta(seconds=duration)

    while datetime.now() < end_time:
        subprocess.run(command, shell=True)
    
    finish_time = datetime.now()
    print(f"Fin de {command} à {finish_time.strftime('%H:%M:%S')}")
    
    with open(log_file, 'a') as log:
        log.write(f"Fin de {command} à {finish_time.strftime('%H:%M:%S')}\n")
        log.write(f"Durée totale : {finish_time - start_time}\n\n")

def benchmark():
    log_file = 'benchmark_log.txt'

    with open(log_file, 'w') as log:
        log.write("Log du benchmark\n\n")

    compile_programs()

    run_program_for_duration("./ray_casting", runtime, log_file)
    time.sleep(pause_duration)

    run_program_for_duration("java RayCasting", runtime, log_file)
    time.sleep(pause_duration)

    run_program_for_duration("java RayCastingAlternative", runtime, log_file)
    time.sleep(pause_duration)

    run_program_for_duration("python ray_casting.py", runtime, log_file)
    time.sleep(pause_duration)

    print("--- Benchmark terminé ---")

if __name__ == "__main__":
    benchmark()

