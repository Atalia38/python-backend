


for i in range(5):
  print("For Loop",i)

y=0
while y<5:
    print("While Loop",y)
    y +=1





    for i in range(5):
        if i == 2:
            continue
        if i == 4: 
            break
        print("Loop Value",i)


    for i in range(3):
        pass

def greet(name):
    message = f"Hello,{name}!"
    return message
print(greet("Atalia"))



def square(x):
    return x*x
square_lambda = lambda x: x * x
print("Lambda Result:", square_lambda(4))


def multiply(a,b):
    return a * b
print(multiply(3,4))


def generate_fib(n):
    fib= [0,1]
    for i in range(2,n):
        fib.append(fib[i-1] + fib[i-2])
    return fib
print(generate_fib(10))



def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)
print("Factorial of 5 is:",factorial(5))
    
