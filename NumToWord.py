class NumToWord:
    def __init__(self,num):
        self.num = num
 
    def ones(self,val):
        num = {'0':'','1':'One','2':'Two','3':'Three','4':'Four','5':'Five','6':'Six','7':'Seven','8':'Eight','9':'Nine'}
        return num.get(val,None)

    def twos(self,val):
        num = {'2':'Twenty','3':'Thirty','4':'Fourty','5':'Fifty','6':'Sixty','7':'Seventy','8':'Eighty','9':'Ninety',}
        num1 = {'10':'Ten','11':'Eleven','12':'Twelve','13':'Thirteen','14':'Forteen','15':'Fifteen','16':'Sixteen','17':'Seventeen','18':'Eighteen','19':'Nineteen',}
        if val[0] != '1':
            return num[val[0]] +" "+ self.ones(val[1])
        else:
            return num1[val]

    def thrice(self,val):
        first = self.ones(val[0])
        if val[1] != '0':
            last = self.twos(val[1:])
        else:
            last = self.ones(val[-1])
            return "{0} Hundred {1}".format(first,last)
        return "{0} Hundred and {1}".format(first,last)
            

        
    def valuate(self):
        if len(self.num) == 1:
            print(self.ones(self.num))
        if len(self.num) == 2:
            print(self.twos(self.num))
        if len(self.num) == 3:
            print(self.thrice(self.num))

if __name__=='__main__':
    num = input('Enter number :')
    num1 = NumToWord(num)
    num1.valuate()
