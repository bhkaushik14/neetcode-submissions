class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(key=lambda x: x[0], reverse=True)

        fleets = []

        for pos, sp in cars:
            time = (target - pos) / sp

            if not fleets:
                fleets.append(time)
            elif time > fleets[-1]:
                fleets.append(time)


        return len(fleets)