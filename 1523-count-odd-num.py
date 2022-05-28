class Solution:
    #https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/
    def countOddsSol1(self, low: int, high: int) -> int:
        #Runs out of memory on very high numbers
        
        #manually insert the numbers for testing without using function
        #low=int(input("Insert low number: "))
        #high=int(input("Insert high number: "))
        num=high-low
        add=low  #will be used to add all the numbers into the list
        numList=[]
        oddList=[]
        #evenList=[]

        for i in range(num+1): #we add 1 so that it counts the high number in the cycle
            numList.append(add)
            add+=1

        for i in range(len(numList)):
            if (numList[i]%2)!=0:
                oddList.append(numList[i])
            #else:
                #evenList.append(numList[i])

        #print(oddList)
        #print(len(oddList))
        #print(evenList)
        #print(len(evenList))

        return len(oddList)
    
    def countOddsSol2(self, low: int, high: int) -> int:
        #Takes too long on very high numbers
        
        #low=int(input("Insert low number: "))
        #high=int(input("Insert high number: "))

        count=0
        var=low
        while var<=high:
            if var % 2 != 0:
                count+=1
                var+=1
            else:
                var+=1
        return(count)
    
    def countOddsSol3(self, low: int, high: int) -> int:
        #This one actually works :)
        
        #low=int(input("Insert low number: "))
        #high=int(input("Insert high number: "))

        if (high-low+1) % 2 == 0:
            res=(high-low+1)/2
            #same amount of odd and even, so can just divide by 2
        elif (high-low+1) % 2 != 0:
            if high % 2 != 0 and low % 2 != 0:
                res=((high-low)/2)+1
            else:
                res=(high-low)/2
        return(int(res))
