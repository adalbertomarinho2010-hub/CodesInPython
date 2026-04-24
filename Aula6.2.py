t = [[1,2], [3], [4,5,6]]
a = t[0] + t[1] + t[2]
print (a)
print (sum(a))
print ("\n")

x = [1,2,3]
y =(sum(x[0:1])), (sum(x[0:2])), (sum(x[0:3]))
print (y)
print ("\n")

Country = ["Alemanha","Itália","Japão"]
Country.append ("Brasil")
print (Country)
print ("\n")

list = [0,1,2,3,4,5,6,7,8,9,10]
print (list[1:10])
print (list[8:11])
print (list[0],list[2],list[4],list[6],list[8],list[10])
print (list[1],list[3],list[5],list[7],list[9])
print (list[0])
list.sort (reverse=True)
print (list)
print (sum(list)) 
print (len(list))
print ("\n")

p1 = (7.0 + 8.3 + 10.0 + 6.5 + 9.3)
p2 = (8.5 + 6.9 + 6.0 + 7.5 + 9.8)
r1 = p1 / 5
r2 = p2 / 5
print ("The average note in the first exam is: %.2f"% (r1))
print ("The average note in the first exam is: %.2f"% (r2))