import random

#taking input of limits from user
a = int(input("enter upper limit: "))
b = int(input("Enter lower limit: "))
x = random.randint(a,b)
print("\n")

print("range is (",a,",",b,") and randomly picked number is ", x)

#to find number is positive or nagative
if (x<0):
  print(x,"is a negative number")
else:
  print(x,"is a positive number")

#to find number is even or odd
if (x%2==0):
  print(x,"is a even number")
else:
  print(x,"is a odd number")

#to find number is prime or not
if (x==0 or x==1):
  print(x, "is neither prime nor composite")
elif (x<0):
  print(x, "is a negative number therefore it is considered composite")
else:
  count=0
  i=2
  while i<= x-1:
    if x % i==0:
      count = count + 1
    i = i+1
  if count == 0:
      print(x,"is a prime number")
  else:
      print(x,"is a composite number")


#done by : jathin chetty(32) , Bommareddy Dhanush(33) , Rajavardhan reddy(34)