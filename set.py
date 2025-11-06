#set
st={1,2,3,2,4,1}
print(st)  # Output: {1, 2, 3, 4}

st1={1,5,1,False,True,0}
print(st1)  # Output: {False, 1, 5}

s1={3,5,2,5,1,2,4,6}
s2={1,2,3,4,5,7}
print("union" , s1.union(s2)) 
print("intersection ", s1.intersection(s2)) 
print("difference" ,s1.difference(s2)) 
print("symmetric_difference", s1.symmetric_difference(s2)) 

print("update" ,s1.update(s2)) 
print("add" ,s1.add(10))

print("remove" ,s1.remove(7))  # This will raise an error since 10 is not in s1
print("discard" ,s1.discard(7))  # This will not raise an error since 10 is not in s1
print("pop" ,s1.pop())  # This will remove and return an arbitrary element from s1
print("clear" ,s1.clear())  # This will remove all elements from s1
print("disjoint" ,s1.isdisjoint(s2))  # This will return True if s1 and s2 have no elements in common
print("issubset" ,s1.issubset(s2)) # This will return True if s1 is a subset of s2
print("issuperset" ,s1.issuperset(s2))  # This will return True if s1 is a superset of s2
