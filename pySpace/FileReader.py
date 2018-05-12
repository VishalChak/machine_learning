class FileReader:
	def __init__(self):
		pass
	def textReader(self, filePath):
		file = open(filePath,"r+")
		lines = file.readlines()
		#for i in range (len(lines)):
		print(len(lines))

if __name__ == "__main__":
	obj = FileReader()
	filePath = "D:\Python\Liability.txt"
	obj.textReader(filePath)