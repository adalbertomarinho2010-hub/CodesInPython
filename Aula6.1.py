one_list = ["a","b","c","d","e","f"]
one_list [1:3] = ["x","y"]
print (one_list)
print ("\n")

another_list = ["a","d","f"]
another_list [1:1] = ["b","c"]
print (another_list)
another_list [4:4] = ["e"]
print (another_list)
print ("\n")

a = ["um","dois","três"]
del a[1]
print (a)
list = ["a","b","c","d","e","f"]
del list[1:5]
print (list)
print ("\n")

b = [81,82,83]
b.append (84)
print (b)
print ("\n")

c = [54,98,90,48,75,60,10]
c.sort()
print (c)
print ("\n")

d = [1,2,3,4,5,6,7,8,9]
print (d.index(5))
print ("\n")

e = [88,81,82,83]
e.insert (4,100)
print (e)
print ("\n")

f = [81,82,88,83,84,88,85,86,88,87,88,89]
print (f)
print (f.count(88))
print ("\n")

g = [81,82,88,83,84,88,85,86,88,87,88,89]
g.pop ()
print (g)
g.pop (0)
print (g)

list2 = [1,2,3] 
list2.extend ([4,5])
print (list2)