'''
list
====
1)List is collection of dissimialr datatype elements.
2)Element in list are enclosed in square brackets.
3)List is mutable.[Once defined they can be changed.]
'''

#define list

l=[10,89.7,-3,45.6,'Itvedant']
print(l)
print (type(l))

#len()

n=len(l)
print("Total number of elements in the list:",n)

#indexing
'''
                       l
                       
          [10,89.7,-3,45.6,'Itvedant']
           0   1    2  3       4
           -5  -4  -3  -2      -1
           
Accessing list element
    syntax:

        list_variable[index_value]
'''

#print(l[3])
#print(l[-4])

#slicing

l1=l[1:4:1]
print(l1)

lrev=l[::-1]
print(lrev)

'''
                       l
                       
          [10,89.7,-3,45.6,'Itvedant']
           0   1    2  3       4

'''
'''
#for loop over list
print("with index:")
                #5
for i in range(0,len(l),1):
    print(l[i])


print("without index:")
for i in l:# [10,89.7,-3,45.6,'itvedant']

    print(i)

'''
#Add element in the list
'''
There are two methods or function to add
element in the list.
1)append():
   This function or method is used to add element at the
   end of the list.
   syntax:
          list_variable.append(element)
2)insert()



'''
#append
#Add element in the list
'''
There are two methods or function to add
element in the list.
1)append():
   This function or method is used to add element at the
   end of the list.
   syntax:
          list_variable.append(element)
2)insert():
  This function or method is used to add element at
  specific index position

  list_variable.insert(index_pos,value)

'''
l.append(24.5)
print(l)

l.append('Eclass')
print(l)

'''
          [10,89.7,-3,45.6,'Itvedant',24.5,'Eclass']
           0   1    2  3       4        5      6


'''

l.insert(3,50)
print(l)

#update list element
'''
2)insert():
  This function or method is used to add element at
  specific index position

  list_variable.insert(index_pos,value)

  syntax:

  list_variable[index_pos]=value
'''

l[4]="Itvedant-Eclass"
print(l)

#delete or remove list elements.
'''
pop(): This is used to delete last elements.

pop(index):This remove specific element whose index is
mentioned in the pop() method.

'''
'''
         [10,89.7,-3,45.6,'Itvedant-Eclass',24.5,'Eclass']
           0   1    2  3       4             5        6
'''

l.pop()
print(l)
'''
         [10,89.7,-3,45.6,'Itvedant-Eclass',24.5]
           0   1    2  3       4             5        

'''
l.pop(2)
print(l)

#del:keyword used to delete entire list at once.

del l
print(l)




































