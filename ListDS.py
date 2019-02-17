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
		
		
	def addToTheEnd(self,listds):
		current=self.headval
		while current.nextval is not None:
			current=current.nextval
		current.nextval=listds
	
	def insertAtSpecificPosition(self,listds,pos):
		current=self.headval
		count=0
		while current.nextval is not None:
			current=current.nextval
			count+=1
			print("Count is ",count)		
			if count == pos:
				break
		temp=current.nextval
		prev=current
		current=listds
		prev.nextval=current
		current.nextval=temp
		
	
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
e5=Node("Thur")
list1.addToTheEnd(e5)
list1.printList()
print("List length after adding new node at the end: ",list1.length())
e6=Node("Fri")
pos=3
list1.insertAtSpecificPosition(e6,pos)
list1.printList()
print("List length after adding new node at the position: ",pos,list1.length())