#class Solution:
#    def countOdds(self, low: int, high: int) -> int:
high=7
low=3
low=int(input("Insert low number: "))
high=int(input("Insert high number: "))
num=high-low
add=low
#count=num
numList=[]
oddList=[]
evenList=[]
'''
while num > low and num < high:
    numList.append(num)
    num+=1
'''
for i in range(num+1):
    numList.append(add)
    add+=1

for i in range(len(numList)):
    if (numList[i]%2)!=0:
        oddList.append(numList[i])
    else:
        evenList.append(numList[i])
print(oddList)
print(len(oddList))
print(evenList)
print(len(evenList))