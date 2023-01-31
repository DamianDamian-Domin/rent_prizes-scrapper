import subprocess
import os
from threading import Thread
from time import perf_counter


# script which runs all spiders simultaneous


wd = os.getcwd()

# define which spiders to run
cities = ['krakow', 'lodz', 'poznan', 'warszawa', 'wroclaw']

# define output folder
output_folder = '02_23'

def runSpiders(output_folder, city):
    subprocess.call( ['bash', '-c', f'./run_spider.sh {output_folder} {city}'], shell=False)

def main():
    threads = [Thread(target=runSpiders, args=(output_folder, city))
                for city in cities]

    for thread in threads:
            thread.start()

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    start_time = perf_counter()

    main()

    end_time = perf_counter()
    print(f'It took {end_time- start_time :0.2f} second(s) to complete.')


