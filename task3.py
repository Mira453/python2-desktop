from array import array

def bubble_sort(arr, reverse = False):
        
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if (arr[j] > arr[j + 1] and not reverse) or (arr[j] < arr[j + 1] and reverse):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr




try:
    input_array = array("f", [2, 6, 4.5, 6, 9, 7]) 
     
    result_growth = bubble_sort(input_array)
    print("Зростаючий масив:", result_growth)
    
    result_decrease = bubble_sort(input_array, reverse=True)
    print("Спадаючий масив:", result_decrease)

except TypeError:
    print("Помилка! Масив повинен містити тільки числові значення.")