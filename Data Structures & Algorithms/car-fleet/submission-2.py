class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
       cars = list(zip(position, speed))
       sorted_cars = sorted(cars, key=lambda x: x[0])

       time_to_arrive = [(target-x[0])/x[1] for x in sorted_cars]

       latest = 0
       fleets = [] 
       print(time_to_arrive)

       for t in time_to_arrive[::-1]:
            fleets.append(t)
            if len(fleets) >= 2 and fleets[-1] <= fleets[-2]:
                fleets.pop()
            
       return len(fleets)

