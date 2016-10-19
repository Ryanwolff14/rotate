list1 = []


def appendList(list):
	listIndex = 0
	while listIndex <= 2:
		list.append(int(input("Enter a number: ")))
		listIndex += 1

	print(list)
	return list

def rotateIndexLeft(list):
	rotatedLeft = list.pop(0)
	list.append(rotatedLeft)
	return list

print(rotateIndexLeft(appendList(list1)))
