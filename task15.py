from datetime import datetime

def sort_students_by_birthdate(students):
    
    sorted_students = tuple(
        sorted(students, key=lambda x: datetime.strptime(x[1], '%d.%m.%Y'))
    )
    return sorted_students

students = (
    ["Іванов Іван Іванович", "15.03.2017"],
    ["Петров Петро Петрович", "23.07.2001"],
    ["Сидорова Анна Сергіївна", "08.11.2006"],
    ["Коваленко Марія Олександрівна", "02.02.1998"]
)

sorted_students = sort_students_by_birthdate(students)
print("Кортеж відсортованний за датами народження: ", sorted_students)