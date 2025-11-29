s1 = {1,2,3}
s2 = s1.copy()

s1.add(4)

print(s1)   #{1, 2, 3, 4}
print(s2)   #{1, 2, 3}

#difference
print('----- difference -----')
print(s1.difference(s2)) #{4}
print(s2.difference(s1)) #empty set

#s1.difference(s2) find out the elements which exist in s1 but not in s2

#difference_update ==> remove the common element of s1 and s2, leaving only the difference.
#note: this update happens in-place so it does modify the original set
print('----- difference update -----')
s1 = {1,2,3}
s2 = {1,4,5}
s1.difference_update(s2)
print(s1) # {2,3}

#discard
print('----- discard -----')
s1 = {1,2,3,5}
s1.discard(5)
print(s1) #{1,2,3}
s1.discard(12)
print(s1) #{1,2,3} | nothing happen since 12 doesn't exist in the set

#intersection
print('----- intersection -----')
print('find the intersection without any in-place modification')
s1 = {1,2,3}
s2 = {1,2,4}
print(s1.intersection(s2)) #{1,2}
print(s1)

print('----- intersection update -----')
print(f's1 before: {s1}') #{1, 2, 3}
s1.intersection_update(s2)
print(f's1 after: {s1}') #{1, 2}

#disjoin
print('----- disjoint -----')
s1 = {1,2,3}
s2 = {1,2,4}
s3 = {5}

#isdisjoint ==> True if no common element
# else ==> False

print(s1.isdisjoint(s2)) #False
print(s1.isdisjoint(s3)) #True

#subset and superset
print('----- subset & superset -----')
s1 = {1,2}
s2 = {1,2,4}

print(s1.issubset(s2)) #True
print(s2.issuperset(s1)) #True

#symmetric_difference and symmetric_update
print('----- symmetric_difference and symmetric_update -----')
#symetric difference return all the elements exist in one set but the other and does not care on the order
s1 = {1,2,3}
s2 = {1,4,5}
print(s1.symmetric_difference(s2)) #{2,3,4,5}
s1.symmetric_difference_update(s2)
print(s1) #{2, 3, 4, 5}

#union
print('----- union -----')
s1 = {1,2,3}
s2 = {1,4,5}
print(s1.union(s2)) #{1,2,3,4,5}

#update
print('----- update -----')
s1 = {1,2,3}
s2 = {1,4,5}
s1.update(s2)
print(s1) #{1,2,3,4,5}