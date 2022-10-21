def avg(a):
	s = 0
	for i in a:
		s += i
	return s / len(a)

def mean(a, index, n):
	if index + n + 1 < len(a):
		return avg(a[index + 1:index + n + 1])
	elif index + 1 < len(a):
		return avg(a[index + 1:])
	else:
		return a[index]
		
def task1():
    a, b = map(int, input().split())
	print((a + b) * (a + b))

def task2():
    s = input()
	k = 0
	for i in s:
	if i.isupper():
	k += 1
	print(k)

def task3():
    s = input()
	a = s.split()
	k = 0
	for i in a:
		if len(i) >= 3:
			if i[0] == "A" and i[1] == "b" and i[2] == "o":
				k += 1
	print(k)

def task4(generator):
    # TODO: четвертое задание

def task5(list_of_smth):
	b = list_of_smth[6::2]
	for i in b:
		print(i, end = " ")

def task6(list1, list2, list3, list4):
    e = []
	f = []
	g = []
	for i in list1:
		e.append(i)
	for i in list4:
		if not i in e:
			e.append(i)
	for i in list2:
		f.append(i)
	for i in list3:
		if not i in f:
			f.append(i)
	for i in e:
		if i in f:
			g.append(i)
	for i in g:
		print(i, end = " ")

def task7():
    import numpy as np
	np.random.seed(1)
	a = np.random.randint(0, 25, (5, 5))
	print(a)
	a = np.delete(a, (0), axis = 0)
	a = np.delete(a,(4),axis = 1)
	print(np.linalg.det(a))

def task8(f, min_x, max_x, N, min_y, max_y):
    # TODO: ...

def task9(data, x_array, y_array):
    # TODO: ...

def task10(list_of_smth, n):
    b = []
	for i in range(len(list_of_smth)):
		b.append(mean(list_of_smth, i, n))
	for i in b:
		print(i, end = " ")

def task11(filename="infile.csv"):
    import numpy as np
	import pandas as pd
	l = df.isnull()
	print(l)
	l = l.sum()
	print(l)
	df['x'] = df['x'].fillna(df['x'].interpolate())
	df['x_err'] = df['x_err'].fillna(df['x_err'].mean())
	print(df)
	df2 = df[df['y'] != np.nan]
	df3 = df2[df2['y_err'] != np.nan]
	print(df3)

def task12(filename="video-games.csv"):
    # TODO: ...

