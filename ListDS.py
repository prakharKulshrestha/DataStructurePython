class Node:
	def __init__(self,dataval=None):
		self.dataval = dataval
		self.nextval = None

class ListDS:
	def __init__(self):
		self.headval = None

	def printList(self):
		printval = self.headval
		print("Inside Print List, Print Val is",printval)
		while  printval is not None:
			print(printval.dataval)
			printval = printval.nextval
		 

print("Hello starting process")
list1 = ListDS()
list1.headval = Node("Mon")
e2 = Node("Tues")
e3 = Node("Wed")
list1.headval.nextval = e2
e2.nextval = e3
list1.printList()