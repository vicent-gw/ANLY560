# Program to display the Fibonacci sequence up to n-th term where n is provided by the user

# change this value for a different result
# nterms = 10

# uncomment to take input from the user
nterms = int(input("How many terms? "))

# first two terms
n1 = 0
n2 = 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence upto",nterms,":")
   while count < nterms:
       print(n1,end=' , ')
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1


# vincent fib func
def fib(n):
  f1,f2 = 0,1
  while n>0:
    f2,f1,n = f1+f2,f2,n-1
    print(f2,end=' , ')

    

