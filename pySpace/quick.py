class Quick:
	listFlag = []
	n = 0
	def insert(self):
		for i in range(self.n):
			self.listFlag.append(int(input()))
	
	def printList(self):
		print ("Array is:")
		for i in range(self.n):
			print(self.listFlag[i])
	
	def qSort (self,i,j):
		if (i <j):
			po = self.partition(i,j)
			self.qSort(i,po-1)
			self.qSort(po+1,j)
			
			
	def partition(self,left,right):
		i = left
		j = right
		while i< j:
			m = (i+j)//2
			mValue = self.listFlag[m]
			while self.listFlag[i] <= mValue and i< j :
				i += 1
			while self.listFlag[j] > mValue :
				j -=1
			if i<j : 
				temp = self.listFlag[i]
				self.listFlag[i] = self.listFlag[j]
				self.listFlag[j] = temp
		self.listFlag[i] = self.listFlag[j]
		self.listFlag[j] = mValue
		return j
		
if __name__ == "__main__":
	obj = Quick()
	obj.n = int(input(" Enter Length"))
	obj.insert()
	obj.printList()
	obj.qSort(0,obj.n-1)
	obj.printList()