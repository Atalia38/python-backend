number = int(input("Enter a number: 11"))

if number < 2 :
    print("Not a prime number")

else:
    prime = True
    # for i in range (2,int(number ** 0.5)+ 1):

    while i <= int(number **  0.5):
    
        if number % i == 0:
            prime = False
            break
        i+=1
        # i +=1    use the while loop
    if prime:
        print("Prime Number")
    else:
        print("Not a prime number")
