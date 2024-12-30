class Employee:
    def __init__(self, name, age, position, pay):
        
        self.name = name
        self.age = age
        self.position = position
        self.pay = pay

    def display_info(self):
        
        return f"Name: {self.name}, Age: {self.age}, Position: {self.position}, Pay: {self.pay}"

    def give_raise(self, amount):
        
        self.pay += amount
        print(f"{self.name} отримав(-ла) підвищення! Нова зарплата: {self.pay}")

    def is_eligible_for_promotion(self, min_age, min_pay):
        
        return self.age >= min_age and self.pay >= min_pay



if __name__ == "__main__":
   
    employee1 = Employee("Іван Іванович", 30, "Інженер", 25000)
    employee2 = Employee("Анна Сергіївна", 45, "Менеджер", 40000)

    print(employee1.display_info())
    print(employee2.display_info())

    employee1.give_raise(5000)

    print(employee1.is_eligible_for_promotion(35, 30000))  
    print(employee2.is_eligible_for_promotion(35, 30000)) 