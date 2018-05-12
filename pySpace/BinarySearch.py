class BinarySearch:
	a = []
	x = 0
	def insert(self,n):
		for i in range (n):
			temp =input("Enetr : ")
			self.a.append(temp)
	def listSort(self):
		self.a.sort()
	def printList (self):
		for i in range(len(self.a)):
			print(self.a[i])
	def Bsearch(self,start,end):
		if start<=end:
			mid = (start + end )//2
			if int(self.a[mid])==x:
				print("Found at  : ",self.a[mid], "  index")
			elif int(self.a[mid])<=x:
				self.Bsearch(mid+1,end)
			else:
				self.Bsearch(start,mid-1)
		else: 
			print("Not Found")
			
if __name__ =="__main__":
	obj = BinarySearch()
	n = int(input("Enter Length of List   "))
	obj.insert(n)
	obj.listSort()
	x= int(input("Enter Key   "))
	obj.x = x
	obj.Bsearch(0,n-1)