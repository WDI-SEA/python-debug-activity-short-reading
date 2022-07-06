#some notes: 
price_cake = '15'
price_cookie = '6'

# String concatenation
total = price_cake + price_cookie
print("The total is: " + total + "$")

# Explicit type conversion to integer
total = int(price_cake) + int(price_cookie)
print("The total is: " + str(total)  + "$")

#The difference between tuples and list is that tuples are immutable, 
# which means once defined you cannot delete, add or edit any values inside it.
a_tuple = (1,2,3,4,5,6,7,8,9,10)
b_list = [1,2,3,4,5]

print("This is tuple >> :",tuple(b_list))
print(list(a_tuple))

#You can also convert a string into a list or a tuple

dessert = 'Cake'

# Convert the characters in a string to individual items in a tuple
print(tuple(dessert))

# Convert a string into a list
dessert_list = list(dessert)
dessert_list.append('s')
print(dessert_list)


a = 79 
bin_a = bin(a)
print("binary here:",bin_a)

oct_a = oct(a)
print(oct_a)