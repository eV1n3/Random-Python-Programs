import time
import os

for hour in range(13):
    for minute in range(61):
        for second in range(61):
            time.sleep(1)
            os.system('cls')
            print(f"{hour}:{minute}:{second}")