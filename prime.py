'''programme to find the whether the number is prime or not '''
num = int(input("enter the number: "));
flag = False;
if(num == 1):
    print("1 is not a prime number: ");
elif(num > 1):
    for i in range(2,num):
        if (num % i  == 0):
            flag = True ;
            break;
if flag :
    print(" the number is not a prime number: ");
else:
    print("The number is a prime number");
        