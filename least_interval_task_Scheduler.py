'''
https://leetcode.com/problems/task-scheduler/

Approach : 
Process the tasks with higher frequency first because if we process them late then they will have to be done in consecutive order mostly and hence lot of idle time 
ex: [a,a,a,b,c] n =2
If we process b , c and then left all 'a' then after every a there will be high idle time
Instead if we process 
a --> b --> c --> a --> idle --> idle --> a [ one of the solution ]
or 
a --> idle --> idle --> a -->b -->c --> a (better solution as it goes in the order of frequencies)

So We would maintain heap to keep track of top task with highest frequency at any given time and then process it

If the tasks with higher frequency can not processed due to "taskTimeTick" > currentTime , then we wait idle 

After processing each task, increment the counter for that task to "currentTime + n" in heap, which is like, when will be this task next available.

Also push the task to queue so that it can be picked in the order in which it needed to be processed. (This is required if at any given time, there are more than one task of same frequency

ex:  [a,a,b,c]
after processing a , we have b,c,a all of same frequency. So we should process first b then c and then a (as it was just processed and end of queue)
)

'''