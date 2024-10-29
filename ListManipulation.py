# Initial list 
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

#step 1: Sort the list in ascending order
numbers.sort()

#step 2:remove all occurences of the number 1 
numbers = [num for num in numbers if num != 1] 

#step 3: add the numbers 7 and 8 to the end of the list 
numbers.extend([7, 8])

#step 4: print the final list
print(numbers)
