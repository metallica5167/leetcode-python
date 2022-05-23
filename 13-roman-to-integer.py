#class Solution:
#    def romanToInt(self, s: str) -> int:
s="XIV"
answer=0
roman={"I":1,"V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

#XIV 012
for i in range(len(s)):
    if i + 1 < len(s) and roman[s(i)] < roman[s(i + 1)]:
        answer=answer-roman[s(i)]
    else:
        answer=answer+roman[s(i)]
print(answer)
#return answer
        


