#class Solution:
#    def countOdds(self, low: int, high: int) -> int:
#manually insert the numbers for testing without using function
low=int(input("Insert low number: "))
high=int(input("Insert high number: "))
num=high-low
add=low #will be used to add all the numbers into the list
numList=[]
oddList=[]
evenList=[]

for i in range(num+1): #we add 1 so that it counts the high number in the cycle
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

#return len(oddList)