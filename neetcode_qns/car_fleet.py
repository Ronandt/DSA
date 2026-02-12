class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #Carfleet not empty
        #car cannot pass another car, only drive limit difference until it catches up
        #considered part if it's at the moment it's at the destination
        #(1,3) (4,2)
        #(4,2), (1,2), (0,1), (7,1)
        #how do you prove that it's gonna become a fleet?
        
        #10-7
        stack = []
        count = len(position)
        the_list = list(sorted(list(zip(position, speed))))[::-1]
        for position,speed in the_list:
            if len(stack) == 0 : #if no items
                stack.append((position,speed))
                continue
            #if the element rn is faster?
            print((target-stack[-1][0])/stack[-1][1], (target-position)/speed)
            if (target-stack[-1][0])/stack[-1][1] >= (target-position)/speed: 
                count -= 1
            else: 
                #what if it's slower/
                stack.pop()
                stack.append((position,speed))
                

                
              



        #might return the length of the stack
        return count

            

            