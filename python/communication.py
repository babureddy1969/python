'''Communication Zones (100 Marks)
Consider a rectangular state of a country. The dimension of the state is M units x N units. The state is divided in M*N cities of dimension 1 unit x 1 unit. See the example.
                                          
As shown in the above example state is 4 unit x 5 unit and there are 4*5=20 cities of 1 unit x 1 unit. Some of the cities have well-established communication and some of the cities have no communication at all. These are shown in the above figure with green and red color respectively. 

Two cities X and Y (Both should be green in color) can communicate with each other if they are directly connected to each other or they are connected to cities X1 and Y1 respectively such that X1 and Y1 are connected. Two cities are said to be directly connected if they share an edge or a corner. So city at (3,1) can communicate to city at (2, 1), (1, 1), (1, 2), (2, 2) and (4, 2). These all connected parts cumulatively form a communication zone. 

Hence, the whole state is divided in various communication zones due to presence of No Communication cities in state. Like in above example, we have two communication zones one in left and one in right.

State Government can stabilize communication in red regions but it would cause some cost and every red region may have a different cost. In fact, there is no use of stabilizing communication in red cities because these are very less populated area. Government concern is to connect the various communication zones. This is possible if some of the red cities are converted into green. So the challenging task for government is that it wants to connect various communication zones in least possible cost.

Example
                                                                    


Every cell is a city and value written in that cell is the cost required to stabilize communication in that city. As shown in the above figure, every green city has value -1 as the cost, it means no cost is required to stabilize communication. But for every red city there is some positive cost associated. There are 4 communication zones in this example, each communication zone consists of only 1 city. The challenge for government is to connect all the 4 communication zones (that too in the least possible cost). This can be done in the various ways; two possible ways are as follows-

                               



Cost for method 1 is 10+10+10=30
Cost for method 2 is only 2

So if we make the red city with cost 2 green it would connect all the four different communication zones. And for the above example, it is the least possible cost.basis.


Input Format
The only line of input consists of a string which contains the cost of converting each city into a green city. It is mentioned in a particular format where all the city cost of rows are separated by '#' and columns are separated by '@' 

For above example, the input string format is specified as -1@10@-1#10@2@10#-1@10@-1  
                                                         
Constraints
1 <= Rows, Columns <= 1000

Output Format
Print minimum possible cost in which all the communication zones can be connected or return 0, if all communication zones are already connected or there is no communication zone.


Sample TestCase 1
Input
-1@10@-1#10@2@10#-1@10@-1
Output
2

'''
s='-1@10@-1#10@2@10#-1@10@-1'
rows=[]
for r in s.split('#'):
	r1= r.split('@')
	r1 = [int(row) for row in r1]
	rows+=[r1]
c=0
for i in rows:
	print (i)
	c+=i.count(-1)
print('initial Connected=',c)
spend=0
