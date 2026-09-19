import array as arr
array_num=arr.array('i',[1,3,5,3,7,9,3])
print("original array:"+str(array_num))
print("number of occurrences of the number3 in the said array:"+str (array_num.count(3)))
array_num.reverse()
print("print the reverse order of the items:")
print(str(array_num))