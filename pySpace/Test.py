class Test:
	def loopTest(self):
		count = 1
		data = []
		while (count >0 and count <2):
			for i in range(4):
				data.append(int(input("Enter feature")))
			print(data)
			data.clear()
			count = int(input())

if __name__ == "__main__":
	obj = Test()
	obj.loopTest()
