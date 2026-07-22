class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Revision ( 22 Jul )
        """
        convert of time array based on position
        whenever you encounter a time more than curr_min add fleet
        """
        pos_speed = [(pos, speed) for pos, speed in zip(position, speed)]
        arrival_time = []
        for position, speed in sorted(pos_speed, reverse=True):
            time = (target - position) / speed
            arrival_time.append(time)
        curr_min = 0
        fleet = 0
        for time in arrival_time:
            if time > curr_min:
                curr_min = time
                fleet += 1

        return fleet
