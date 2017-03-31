##Basic program

# Hello world program
print('Hello World!')



## Program on Conditional statements

answer=4                  #set a value 4 for the variable 
if answer>5:
	val1=1
	print(val1)
elif answer<5:           #prints -1, since 4<5 
	val2=-1
	print(val2)
else:
	val3=0
	print(val3)
	 

##Program on functions
def greet(name):
	"""This function greets to
	the person passed in as
	parameter and uses multiline comments"""
	print("Hello, " + name + ". Good morning!")

greet('Paul')


##Program for lambda function
double = lambda x: x * 2 #Here, 'x' is argument,'x*2' is expression that gets evaluated and returned
print(double(5))


##Program on lists
 
list = ['56','WHITE',2000,'Red','BLUE']
print list 								# Prints entire list
print (list[2])                         # Prints only element that index 2
list.append(23)                         # Adds 23 to the list
print list   
list.insert(2,"Orange")                 # Adds 'Orange' to the list at index 2
print list 
del list[2]                             # Deletes element at index 2
print list 
del list				   				# Deletes entire list
 
##Program using for-loop	
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]
sum = 0
for val in numbers:           			# iterate over the list
	sum = sum+val
print("The sum is", sum)


##Program using while-loop
n = 10
sum = 0
i = 1
while i <= n:
    sum = sum + i
    i = i+1    # update counter
print("The sum is", sum) 
