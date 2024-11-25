from array import array
import random

def RandomArray(N):
    if not isinstance(N, (int, float)):
        print("Помилка! N повинно бути числом.")
        return None
    
    arr = array("f", [])
    while len(arr) < N:
        num = random.randint(1, N)
        if arr.count(num) == 0:
            arr.append(num)
    return arr


N = 68
if not RandomArray(N) == None:
    print("Масив: ", RandomArray(N))