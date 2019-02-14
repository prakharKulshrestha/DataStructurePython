class Node:
	def __init__(self,dataval=None):
		self.dataval = dataval
		self.nextval = None

class ListDS:
	def __init__(self):
		self.headval = None

	def printList(self):
		printval = self.headval
		while  printval is not None:
			print(printval.dataval)
			printval = printval.nextval
		 
	def length(self):
		len=0
		printval = self.headval
		while  printval is not None:
			printval = printval.nextval
			len+=1
		
		return len
	
	def addToBeginning(self,listds):
		temp=self.headval
		self.headval=listds
		self.headval.nextval=temp
		
		 

list1 = ListDS()
list1.headval = Node("Mon")
e2 = Node("Tues")
e3 = Node("Wed")
list1.headval.nextval = e2
e2.nextval = e3
list1.printList()
print("List length before adding new node at the beginning: ",list1.length())
e4=Node("Sun")
list1.addToBeginning(e4)
list1.printList()
print("List length after adding new node at the beginning: ",list1.length())