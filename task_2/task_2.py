# Why does print_list() not correctly print out the elements a_list?
# Because the lenght of the list and the number of steps in range() do not
# match. range() does not include the stop parameter's last
# position.
# Why don't we start the range from 0? This would be the defaut in range()
# function.

def print_list(a_list):
    for i in range(len(a_list)):
        print('Element {} = {}'.format(str(i),str(a_list[i])))

a_list = [1, 2, 3, 5, 7, 9]

print("--- first option ---")
print_list(a_list)

# Now, programmers will say that this is correct:
# Element 0 = 1
# Element 1 = 2
# Element 2 = 3
# Element 3 = 5
# Element 4 = 7
# Element 5 = 9

# Or, if we want to list all elements from 1, because, let's say
# we're printing this out for people unrelated to programming).

def print_list_second_option(a_list):
    z = 1 + len(a_list)
    for i in range(1, z):
        print('Element {} = {}'.format(str(i),str(a_list[i-1])))

a_list = [1, 2, 3, 5, 7, 9]
print("--- second option ---")
print_list_second_option(a_list)

# Then this will be the result:
# Element 1 = 1
# Element 2 = 2
# Element 3 = 3
# Element 4 = 5
# Element 5 = 7
# Element 6 = 9