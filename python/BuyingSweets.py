'''Cimpress Code Canvas

Buying Sweets (100 Marks)
Sachin likes sweets a lot. So, he goes to a market of sweets. There is a row of sweet stalls. Every sweet stall has different sweets. To save some time, he decided to buy sweets from contiguous stalls. So, he can buy from as many stalls as he wants, but all of those stalls need to be contiguous. He also decided to buy only 1 kg of sweets from each of those stalls. Cost of 1 kg of sweets for each stall is given. There is a strange rule of billing in that market. And that rule is as follows- Total cost of all sweets bought is sum of the cost of all sweets multiplied by the cost of sweet he bought at the end. e.g. if he buys sweets having cost 2, 3, 4 in the same order than total cost of sweets will be 2*4+3*4+4*4=36. Now he wonders what will be the total cost of all possible ways of buying sweets. Can you help him. Because this number could be large, you should take modulo of the final result by 10^9+7.


Input Format
Your function contains a single argument- A One dimensional Integer array of Size N in which ith element denotes the cost of 1 kg sweets from ith stall.
First line of input contains an Integer N denoting the size of Array. 
Next N lines of input each containing a single integer from 1 to 9.


Constraints
1<=N<=10^5

Output Format
You must return an integer- sum of the cost of all possible ways of buying sweets modulo 10^9+7.


Sample TestCase 1
Input
3
1
2
3
Output
53
Explanation
Possible ways of buying sweets are-
a) 1
b) 1 2
c) 2
d) 1 2 3
e) 2 3
f) 3
cost of each of these is following-
a) 1*1= 1
b) 1*2+2*2= 6
c) 2*2= 4
d) 1*3+2*3+3*3= 18
e) 2*3+3*3= 15
f) 3*3= 9

Hence total cost will be 1+6+4+18+15+9=53'''

def main():

    n=int(input(''))
    L=[]
    for i in range(1,n+1):
        L += [i]
    combo= [L[i:i+j] for i in range(len(L)) for j in range(1,len(L)-i+1)]
    #print(combo)
    sum=0
    for l in combo:
        for u in l:
            sum += u*l[-1]
    print(sum)
main()

