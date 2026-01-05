#functon
'''
def greet():
    print("Hello good mornig")

greet()


def marriage(boy, girl):
    print(f"boy is {boy}")
    print(f"girl is {girl}")
    print(f"{boy} married {girl}")

marriage("Adarsha","Ranjitha") #Positional arguments
marriage("Krishna", "Ranjitha")
marriage(boy="Adarsha", girl="Ranjitha") #keword arguments
'''

def tables(num):
    for i in range(1,11):
        print(f"{num}X{i}={num*i}")
tables(4)