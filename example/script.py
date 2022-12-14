import time
from pathlib import Path
import ruslat

pth = Path(__file__).absolute().parent

start_time = time.perf_counter()

with open(pth/'Обломов.txt', 'r', encoding='utf-8') as cyr,\
    open(pth/'Oblomov.txt', 'w', encoding='utf-8') as lat:
    for line in cyr:
        lat.write(ruslat.latinizator(line))

print("Execution time:", time.perf_counter() - start_time, "seconds")