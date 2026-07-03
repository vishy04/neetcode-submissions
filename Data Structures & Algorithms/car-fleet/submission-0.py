class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        #look the the car closest to the target
        #merge position and speed
        # car_pos = list(zip(position, speed))

        car_pos = [(p,s) for p,s in zip(position,speed)]

        fleet = 0
        bottle_neck = 0
        for pos,speed in sorted(car_pos,reverse = True): 
            time_of_arrival = (target - pos)/speed
            if time_of_arrival > bottle_neck :
                bottle_neck = time_of_arrival
                fleet += 1
        
        return fleet
            