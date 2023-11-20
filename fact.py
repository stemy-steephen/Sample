def fact(n):
   if n == 1:
       return 1
   elif n==0:
        print("error")
   else:
       return n*fact(n-1)
n=int(input("enter a number"))
x=fact(n)
print(x)

num = int(input("Enter a number: "))    

def fact(num): 
   factorial = 1    
   if num < 0:    
      print(" error")    
   elif num == 0:    
      return 1   
   else:    
        for i in range(1,num + 1):    
            factorial = factorial*i    
        print(factorial)  
fact(n)

num = int(input("Enter the number: "))
def prime(num):
   if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                print(num,"is not a prime number")
                break
            else:
                print(num,"is a prime number")
   else:
    print(num,"is not a prime numb")
prime(n)