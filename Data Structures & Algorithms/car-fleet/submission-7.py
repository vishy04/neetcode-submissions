class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #Revision( Stack )
        # We only care about monotonic increasing value storage

        time_stack = []
        #pos_speed = 
        pos_speed = [(p,s) for p,s in zip(position,speed)]
        time_stack = []
        for pos , speed in sorted(pos_speed,reverse = True):
            time = (target - pos) / speed
            if not time_stack or time > time_stack[-1]:
                time_stack.append(time)
        
        return len(time_stack)