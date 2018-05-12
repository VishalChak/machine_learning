from Stack import *
class Num2Word:
	num2words = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \
             6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', \
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', \
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', \
            19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty', \
            50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', \
            90: 'Ninety', 0: 'Zero'}
	def convert(self,num,stack):
		if num == 0 :
			print(stack.items)
		elif 0<num<=19:
			stack.push(self.num2words[num])
			print(stack.items)
		else :
			stack.push(self.num2words[num%10])
			self.convert(num//10,stack)
	def reverceS(self,item):
		j = len(item)-1
		for i in range (len(item)//2):
			temp = item[i]
			item[i] = item[j]
			item[j] = temp
			
if __name__ == "__main__":
	stack = Stack()
	obj = Num2Word()
	x = input("Enter Num")
	item = list(x)
	obj.reverceS(item)
	obj.convert(int(str(item)),stack)
	