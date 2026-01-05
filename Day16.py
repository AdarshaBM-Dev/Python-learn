'''
cledef add(*numbers):
    return sum(numbers)

print(add(1,100,45))



#varible length arguments
def studen_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

studen_info(name="Anand", age=22, course="python")

#lambda funcunctions
add = lambda a,b : a+b
print(add(1,2))

double = lambda x: 2*x
print(double(200))

students = [
    {"name":"Anand", "marks":70},
    {"name":"Adarsha", "marks":100},
    {"name":"Surya", "marks":50}
]
students.sort(key= lambda x: x["marks"])
print(students)
students.sort(key= lambda x: x["marks"], reverse= True)
print(students)

#recursion
def factorial(n):
    if n==1:
        return 1
    return n * factorial(n-1)
print(factorial(3))
'''

#nested functios
def calculate(a,b):
    def add():
        print(a+b)
    def sub():
        print(a-b)
    def mult():
        print(a*b)
    add()
    sub()
    mult()
calculate(10,2)