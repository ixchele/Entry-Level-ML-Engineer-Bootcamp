from tqdm import tqdm
from time import sleep

def ft_progress(listy):
    for elem in tqdm(listy, ascii=" >=", 
                     bar_format="ETA: {remaining_s:.2f}s [{desc}: {percentage:3.0f}%][{bar}] {n_fmt}/{total_fmt} | elsapsed time {elapsed_s:.2f}s"):
        yield elem

listy = range(1000)
ret = 0
for elem in ft_progress(listy): 
    ret += (elem + 3) % 5
    sleep(0.01)
print()
print(ret)
