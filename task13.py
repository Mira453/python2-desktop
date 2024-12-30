def find_unique_words(list1, list2):

    set1 = set(list1)
    set2 = set(list2)

    unique_words = list((set1 - set2) | (set2 - set1))
    return unique_words

list1 = ["apple", "banana", "cherry", "date"]
list2 = ["banana", "cherry", "elderberry", "fig"]

result = find_unique_words(list1, list2)
print(result)