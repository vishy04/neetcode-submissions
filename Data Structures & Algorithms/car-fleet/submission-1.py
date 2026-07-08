class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        INTUITION: The Monotonic Stack (Filtering the noise)

        Working backwards from the target, a fast car will always catch up
        and merge with a slower car ahead of it. Therefore, we only care
        about the "bottlenecks" — the strictly slower times.

        Eg: Time of Arrival = [3, 3, 4.5, 3, 4, 9, 8, 10, 7]
        Bottlenecks (Fleets) = ^      ^         ^      ^

        By building a strictly increasing stack, we naturally filter out absorbed cars:
        1. Push 3 -> Stack: [3]
        2. Ignore numbers <= 3. (They catch up to the '3' fleet).
        3. See 4.5. It's strictly > 3, so it forms a new fleet! -> Stack: [3, 4.5]
        4. Ignore 3 and 4. (They catch up to the '4.5' fleet).
        5. See 9. Push -> Stack: [3, 4.5, 9]
        6. See 10. Push -> Stack: [3, 4.5, 9, 10]

        The items that survive in the stack represent the distinct fleets.
        Result = len(stack).
        """

        time_of_arrival = []

        # we want to sort it reversed based on position
        pos_speed = [(p, s) for p, s in zip(position, speed)]

        for pos, speed in sorted(pos_speed, reverse=True):
            time_of_arrival.append((target - pos) / speed)

        stack = [time_of_arrival[0]]
        for time in time_of_arrival:
            # only if current time is more than the top of stack
            if time > stack[-1]:
                stack.append(time)

        return len(stack)
