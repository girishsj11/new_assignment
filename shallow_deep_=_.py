import copy  #to perform deepcopy & shallow copy we import the copy module

# '=' operator example
#Way 1: normal list or single dimensional list
lst1 = [1,2,3,4,5]
lst2 = lst1
print("Before doing the changes on the normal list with '=' operator")
print(f"list1 - {lst1} & list2 - {lst2}")
lst2[1] = 100
print("After doing the changes on the normal list with '=' operator")
print(f"list1 - {lst1} & list2 - {lst2}")
print(f"ids of list : lst1 - {id(lst1)} , lst2 - {id(lst2)}")
'''
#output -
Before doing the changes on the normal list with '=' operator"-
list1 - [1, 2, 3, 4, 5] & list2 - [1, 2, 3, 4, 5]
After doing the changes on the normal list with '=' operator"-
list1 - [1, 100, 3, 4, 5] & list2 - [1, 100, 3, 4, 5]
'''

#Way 2: nested list or multi dimensional list
lst1 = [1,2,3,[4,5],6,[7,8,2]]
lst2 = lst1
print("Before doing the changes on the nested list with '=' operator")
print(f"list1 - {lst1} & list2 - {lst2}")
lst2[5][2] = 100
print("After doing the changes on the nested list with '=' operator")
print(f"list1 - {lst1} & list2 - {lst2}")
print(f"ids of list : lst1 - {id(lst1)} , lst2 - {id(lst2)}")
'''
#output - 
Before doing the changes on the nested list with '=' operator-
list1 - [1, 2, 3, [4, 5], 6, [7, 8, 2]] & list2 - [1, 2, 3, [4, 5], 6, [7, 8, 2]]
After doing the changes on the nested list with '=' operator-
list1 - [1, 2, 3, [4, 5], 6, [7, 8, 100]] & list2 - [1, 2, 3, [4, 5], 6, [7, 8, 100]]
'''



#Shallow copy example
print("\n")
lst1 = [1,2,3,4,5]
lst2 = lst1.copy()
print("Before doing the changes on the normal list with list.copy() function")
print(f"list1 - {lst1} & list2 - {lst2}")
lst2[1] = 100
print("After doing the changes on the normal list with list.copy() function")
print(f"list1 - {lst1} & list2 - {lst2}")
print(f"ids of list : lst1 - {id(lst1)} , lst2 - {id(lst2)}")
'''
#output -
Before doing the changes on the normal list with list.copy() function-
list1 - [1, 2, 3, 4, 5] & list2 - [1, 2, 3, 4, 5]
After doing the changes on the normal list with list.copy() function-
list1 - [1, 2, 3, 4, 5] & list2 - [1, 100, 3, 4, 5]
'''

#Way 2: nested list or multi-dimensional list
lst1 = [1,2,3,[4,5],6,[7,8,2]]
lst2 = lst1.copy()
print("Before doing the changes on the nested list with list.copy() function")
print(f"list1 - {lst1} & list2 - {lst2}")
lst2[5][2] = 100
print("After doing the changes on the nested list with list.copy() function")
print(f"list1 - {lst1} & list2 - {lst2}")
print(f"ids of list : lst1 - {id(lst1)} , lst2 - {id(lst2)}")
'''
#output - 
Before doing the changes on the nested list with list.copy() function-
list1 - [1, 2, 3, [4, 5], 6, [7, 8, 2]] & list2 - [1, 2, 3, [4, 5], 6, [7, 8, 2]]
After doing the changes on the nested list with list.copy() function- 
list1 - [1, 2, 3, [4, 5], 6, [7, 8, 100]] & list2 - [1, 2, 3, [4, 5], 6, [7, 8, 100]]
'''



#Deepcopy example
print("\n")
lst1 = [1,2,3,4,5]
lst2 = copy.deepcopy(lst1)
print("Before doing the changes on the normal list with copy.deepcopy function")
print(f"list1 - {lst1} & list2 - {lst2}")
lst2[1] = 100
print("After doing the changes on the normal list with copy.deepcopy function")
print(f"list1 - {lst1} & list2 - {lst2}")
print(f"ids of list : lst1 - {id(lst1)} , lst2 - {id(lst2)}")
'''
#output -
Before doing the changes on the normal list with copy.deepcopy function-
list1 - [1, 2, 3, 4, 5] & list2 - [1, 2, 3, 4, 5]
After doing the changes on the normal list with copy.deepcopy function-
list1 - [1, 2, 3, 4, 5] & list2 - [1, 100, 3, 4, 5]
'''

#Way 2: nested list or multi dimensional list
lst1 = [1,2,3,[4,5],6,[7,8,2]]
lst2 = copy.deepcopy(lst1)
print("Before doing the changes on the nested list with copy.deepcopy function")
print(f"list1 - {lst1} & list2 - {lst2}")
lst2[5][2] = 100
print("After doing the changes on the nested list with copy.deepcopy function")
print(f"list1 - {lst1} & list2 - {lst2}")
print(f"ids of list : lst1 - {id(lst1)} , lst2 - {id(lst2)}")
'''
#output - 
Before doing the changes on the nested list with copy.deepcopy function-
list1 - [1, 2, 3, [4, 5], 6, [7, 8, 2]] & list2 - [1, 2, 3, [4, 5], 6, [7, 8, 2]]
After doing the changes on the nested list with copy.deepcopy function- 
list1 - [1, 2, 3, [4, 5], 6, [7, 8, 2]] & list2 - [1, 2, 3, [4, 5], 6, [7, 8, 100]]
'''
