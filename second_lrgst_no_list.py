# Python program to find second largest number
# in a list
l1=int(input("Enter the number for list1:-"))
l2=int(input("Enter the number for list2:-"))
l3=int(input("Enter the number for list3:-"))
l4=int(input("Enter the number for list4:-"))
l5=int(input("Enter the number for list5:-"))
l6=int(input("Enter the number for list6:-"))
l7=int(input("Enter the number for list7:-"))
# List of numbers
list = [l1, l2, l3, l4,l5, l6,l7]
 
#new_list is a set of list
new_list = set(list)

# Removing the largest element from temp list
new_list.remove(max(new_list))

# Elements in original list are not changed
# print(list)
print(max(new_list))
