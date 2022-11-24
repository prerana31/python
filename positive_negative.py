'''
From the give list filter positive and negative elements and
create two list.

         [1,-9,89,76,-56,-3,0,12,15,167,-8,2]

If a number is greter than 0 then it is positive
If a number if less than 0 then it is negative.
'''

l=[1,-9,89,76,-56,-3,0,12,15,167,-8,2]
lpos=[]
lneg=list()  #constructor
for x in l:
    #print(x)

    if x>0:#positive
        lpos.append(x)

    else:
        lneg.append(x)

print("positive list:",lpos)
print("negative list:",lneg)

'''                   
                            l
            [1,-9,89,76,-56,-3,0,12,15,167,-8,2]

        lpos                   lneg
        [1,89,76]             [-9]
        
x  x in []    x>0                            else
1  1 in []T   1>0=>lpos.append(1)            -
-9 -9in []T  -9>0                           lneg.append(-9)
89 89in []T  89>0=>lpos.append(89)          -
76 76in []T  76>0=>lpos.append(76)

'''











