def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

print('select an operation:')
print('1.add')
print('2.subtract')
print('3.multiply')
print('4.divide')

while True:
    choice = input('Enter choice: ')
    if choice in ('1','2','3','4'):
        try:
            num1 = float(input('Enter first number: '))
            num2 = float(input('Enter second number: '))
        except ValueError:
            print('Please enter a valid number')
            continue
        if choice == '1':  
            print(num1,'+',num2,'=',add(num1,num2))   
        elif choice == '2':
            print(num1,'-',num2,'=',sub(num1,num2))
        elif choice == '3':
            print(num1,'*',num2,'=', mul(num1,num2)) 
        elif choice == '4':
            print(num1,'/',num2,'=', div(num1,num2)) 
        
        
        next_calculation = input("Let's do next calculation? (yes/no): ")

        if next_calculation == "no":
          print('Goodbye!')
          break
    else:
        print("Invalid Input")
