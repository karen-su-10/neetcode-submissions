class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #go through the car array, sorted from if time current >= time previous,a new fleet, add to car_fleet stack. Monotonic Stack（单调栈） 模式：Stack 中的时间严格递增
        # Pair by zip, the sort by 1st element, from small to larg, reverse is from large to small. the large the position the close to the target
        cars = sorted(zip(position, speed), reverse=True)

        car_fleet = []

        for pos, spd in cars:
            time = (target - pos) / spd

            if not car_fleet:
                car_fleet.append(time)

            elif time > car_fleet[-1]:
                car_fleet.append(time)

        return len(car_fleet)


            