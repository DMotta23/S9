a = [1,2,3]
a.append(7)
a.append("Bob")
print(a)
a[1] = "Campbell"
print(a)
#extend is the same as append but adds another list
a.extend(["James","Bond"])
print(a)

a.pop(4) #pops from index
print(a)