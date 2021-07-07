#nums=[1,2,3,4,5,6,7,8,9,10]
#I want 'n' for each 'n' in nums
#my_list=[]
#copied each element from nums into my_list
#for n in nums:
#    my_list.append(n)
#print(my_list)

#list comprehension
#its the same as above but less code
#my_list=[n for n in nums]

#i want 'n*n' for each 'n' in nums
'''my_list=[]
for n in nums:
    my_list.append(n*n)
print(my_list)'''

#the above code in list comprehension
#my_list=[n*n for n  in nums]
#print(my_list)


#I want 'n' for each 'n' in nums if 'n' is even
'''my_list=[]

for n in nums:
    if(n%2==0):
        my_list.append(n)
        
print(my_list)'''

#list comprehension
#my_list=[n for n in nums if n%2==0]
#print(my_list)

#using filter + lambda
#my_list=filter(lambda n : n%2==0, nums)


#I want a (letter,nums) pair for each letter in 'abc' and each number in '0123'
'''my_list=[]
for letter  in 'abcd':
    for num in range(4):
        my_list.append((letter,num))
'''

#list comprehension
#my_list=[(letter,num) for letter in 'adbcd' for num in range(4)]
#print(my_list)

#dictionary comprehension
#names=['Bruce','Clark','Peter','Logan','wade']
#hero=['batman','Superman','Spiderman','Wolverine','Deadpool']
#print(zip(names,hero))

#I want a dict{'name':'hero'} for each name,hero in zip(names,heros)
'''my_dict={}
for name, hero in zip(names,hero):
    my_dict[name]=hero
'''

#dictionary comprehension
#my_dict={name:hero for name,hero in zip(names,hero) }
#print(my_dict)

#If i name not equal to Peter
#my_dict={name:hero for name,hero in zip(names,hero) if name != 'Peter'}
#print(my_dict)

#Set comprehensions
#set's have all unique values
#nums=[1,1,2,1,3,4,3,4,5,5,6,7,8,7,9,9]
'''my_set=set()
for i in nums:
    my_set.add(i)
print(my_set)'''

#set comprehension
#my_set={n for n in nums}
#print(my_set)

nums=[1,2,3,4,5,6,7,8,9,10]
