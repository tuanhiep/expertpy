# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Tuan Hiep TRAN')

# initializing string
test_string = "geekforgeeks"

# printing original string
print("The original string : " + str(test_string))
print(sorted(test_string))
# using join() + sorted()
# Sorting a string
res = ''.join(sorted(test_string))

# print result
print("String after sorting : " + str(res))

dict = {'Sex': 'female', 'Age': 7, 'Name': 'Zara'}
print (list(dict.values()))
print (dict.values())
