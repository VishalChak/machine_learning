class Dutch:
	listFlag = []
	n = 0
	def insert(self):
		for i in range(self.n):
			self.listFlag.append(int(input()))
	
	def printList(self):
		print ("Dutch Nation Flag is : : ")
		for i in range(self.n):
			print(self.listFlag[i])
	
	def arrangeFlag(self):
		i = 0
		j = self.n-1
		while i< j:
			while self.listFlag[i]%2 == 0 :
				i += 1
			while self.listFlag[j] %2 != 0 :
				j -=1
			if i<j : 
				temp = self.listFlag[i]
				self.listFlag[i] = self.listFlag[j]
				self.listFlag[j] = temp
			
		
if __name__ == "__main__":
	obj = Dutch()
	obj.n = int(input(" Enter Length"))
	obj.insert()
	obj.printList()
	obj.arrangeFlag()
	obj.printList()