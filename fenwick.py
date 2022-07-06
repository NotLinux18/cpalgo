import os
os.system('clear')

n = int(input("Enter the size : "))

array = [0] * (n+1)
tree = [0] * (n+1)

for i in range (n) : 
	array[i+1] = int(input(f"Enter the element {i+1} : "))

def update(val , pos) : 
	while pos <= n : 
		tree[pos] += val
		pos += pos & (-pos)

def sum(pos) : 
	ans = 0;
	while pos > 0 : 
		ans += tree[pos]
		pos -= pos & (-pos)
	return ans

for i in range (n) : 
	update(array[i+1] , i+1)

q = int(input("Enter the query number : "))
print("______________________________")
print("Query types : ")
print("type '1' ===> update , index and the value you increment it by : ")
print("type '2' ===> query , left and right , the interval you want its sum : ")
print("Note : all of these are inclusive ")
print("______________________________")
for dumb in range(q) : 
	type = int(input("Enter the type : "))
	if type == 1 : 
		ind = int(input("Enter the index : "))
		cha = int(input("Enter the value : "))
		update(cha , ind)
	else : 
		left = int(input("Enter the left : "))
		right = int(input("Enter the right : "))
		print(sum(right) - sum(left-1))

