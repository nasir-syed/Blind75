def robthem(houses):
     rob1, rob2 = 0, 0

     r1 = []
     r2 = []

     # [rob1, rob2, n, n+1, ...]
     for n in houses:
         temp = max(n + rob1, rob2)
         rob1 = rob2
         r1.append(rob1)
         rob2 = temp
         r2.append(rob2)


     print("rob1: ",r1,"\t\trob2: ", r2)
     return rob2

houses = [1,2,3,1]
print(robthem(houses)) # 1+3 (can't rob adjacent houses so mo 2, choosing between 3 and 1)
