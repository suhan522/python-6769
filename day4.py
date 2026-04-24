
print('----------------List-------------')

a = [1,2,3,4,5]

print(type(a))
data = ['hello',1,True,1.5]
print(data)

print(data[1])
print(data[-1])


# -4 <-----> 3
print (len(data))

teacher = ('prem,raju,purna,bhim,ghanshyam,rita,aarush')
print(teacher[1:5])
print(teacher[1:])
print(teacher[:5])
print(teacher[:])


#insert
#extend
#concat
#append

#append

a = [1,2,3]
a.append(5)
a.append(6)
print(a)

item = []
item.append(12)
item.append(13)

print(item)

#insert
peoples = ['samir,sushant,jenish,pranesh,aarush']
peoples.insert(1,'hari')
print(peoples)

peoples.insert(100,'test')
print(peoples)

#extend
a = [1,23,4]
b = [5,6,7]
#[1,23,4,5,6,7]
b.extend(a)
a.extend(b)
print(a)
print(b)

#concat
a = (1,2,3)
b = [5,6,7]
print(a,b)

#del
#pop
#remove
#clear

#del
data = [1,23,4,5,6,7]
del data [0]

print(data)

#pop
remove_data = data.pop()
print(data)
print(remove_data)

#item = []
#item.pop()
#print(item)

#remove
a = [1,2,3,4,5]
a.remove(4)
a.remove(2)
#a.remove(20) error case


#clear
data = ('aarush','jenish','prabhaav','nwan','suraj')
data.clear()
print(data)

data = ['aarush','prabhaav','manish','suraj','nwan']
print(data.count('haris'))
print(data.index('Haris'))

data.sort(reverse=True)
print(data)
data = ('Aarush','suraj','nwan','jenish')

data.reverse()
print(data)

b = [5,6,7,7,[1,2,3]]
print(len(b))
item = b[4]
print(item[1])