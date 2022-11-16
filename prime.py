
'''
A numebr which is completely divisible by 1 and itself is called as prime number

7 is prime number=> 7 is completely divisible by 1 and 7

8 is also completly divisible by 1 and 8, but 8 is non prime number.

n=7

   1     2 3 4 5 6    7
         ---------
  excluding 1 and 7 check whether any number completly divides 7, so none of in between numbers completly divides 7, thus
  it is prime number.

n=9

   1    2 3 4 5 6 7 8   9
'''

n=int(input("enter number"))
for i in range(2,n,1):#(2,6,1)=>[2,3,4,5]
    r=n%i
    if r==0:
        print("non prime number")
        break
