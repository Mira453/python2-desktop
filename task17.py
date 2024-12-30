class Student:

    def __init__(self, name =&quot;John Doe&quot;, courses =[]):
    self.name = name
    self.courses = courses
    print(&quot;Створено об’єкт для &quot;+ name)
    
    def printDetails(self):
    print(&quot;Ім’я: &quot;, self.name)
    print(&quot;Курси: &quot;, self.courses)
    def enroll(self, course):

    self.courses.append(course)
    student1 = Student(&quot;Mary&quot;, [&quot;L548&quot;])
    print(&quot;Уведіть курси, які вивчає&quot;, student1.name)
    newcourse = input (&quot;Уведіть номер курсу або &#39;stop&#39; &quot;)
    while newcourse != &quot;stop&quot;:
    student1.enroll(newcourse)
    print(&quot;Уведіть курси, які вивчає&quot;, student1.name)
    newcourse = input (&quot;Уведіть номер курсу або &#39;stop&#39; &quot;)
    tudent1.printDetails()