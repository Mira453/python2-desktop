from array import array

def create_array(*args):
    arr = array("i", [])
    
    for arg in args:
        
        if isinstance(arg, int) == True:
            arr.append(arg)
        else:
            print("Помилка! В масиві повинні бути тільки цілі числа.")
            return None
            
    return arr
    
result = create_array(2, 7, 45, 10)
if result is not None:
    print("Створений масив:", result)