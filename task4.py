from array import array

def check_array(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True
        
        
def joins_array(arr1, arr2):
    if check_array(arr1) and check_array(arr2):
        merged_array = arr1 + arr2   
        n = len(merged_array)
        for i in range(n):
            for j in range(0, n - i - 1):
                if (merged_array[j] > merged_array[j + 1]):
                    merged_array[j], merged_array[j + 1] = merged_array[j + 1], merged_array[j]
        return print("Об'єднаний масив: ", merged_array)
    else:
        print("Помилка! Масив повинен бути впорядкований за зростанням.")
        
def includes_el_arry(arr1, arr2):
    if check_array(arr1) and check_array(arr2):
        arr1.extend(arr2)   
        n = len(arr1)
        for i in range(n):
            for j in range(0, n - i - 1):
                if (arr1[j] > arr1[j + 1]):
                    arr1[j], arr1[j + 1] = arr1[j + 1], arr1[j]
        return print("Перший масив включає елементи другого масиву: ", arr1)
    else:
        print("Помилка! Масив повинен бути впорядкований за зростанням.")      
            

array1 = array("f", [1, 3.5, 8, 9, 10])
array2 = array("f", [2, 3, 4, 5])

joins_array(array1, array2)
includes_el_arry(array1, array2)