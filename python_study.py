

from typing import Any
import random



class Map:
    def __init__(self, rows: int, cols: int, start, stop) -> None:
        self.rows = rows
        self.cols = cols
        self.start_location = start
        self.stop_location = stop
        self.map = self._generate_map(rows,cols)


    def _generate_map(self, rows, cols):
        map = [[random.randint(0, 1) for _ in range(cols)] for _ in range(rows)]
        map[self.start_location[0]][self.start_location[1]] = 0
        map[self.stop_location[0]][self.stop_location[1]] = 0
        return map

    def display_map(self):
        for row in self.map:
            print(row)


class Car:
    def __init__(self, location_x: int, location_y: int, map: Map, main = False, has_arrived = False) -> None:
        self.main = main
        self.location_x = location_x
        self.location_y = location_y
        self.has_arrived = has_arrived
        self.map = map
    
    def place_car_in_map(self, map: Map) -> None:
        map.map[self.location_x][self.location_y] = "Car"

    def car_move(self, next_location: (int, int)) -> None:
        self.map.map[self.location_x][self.location_y] = 0
        self.location_x, self.location_y = next_location
        self.map.map[self.location_x][self.location_y] = "Car"




def set_fixed_location(rows, cols) -> (int, int):
    return (random.randint(0, rows -1 ), random.randint(0, cols -1 ))

def surroundings(x_location, y_location):
    return [(x_location, y_location + 1), (x_location, y_location - 1), (x_location + 1, y_location), (x_location - 1, y_location)]

def path_planning(start, stop, map):
    start_x, start_y = start
    stop_x, stop_y = stop
    path = []
    stack = [(start_x, start_y)]
    visited = set()
    while stack:
        x, y = stack.pop()
        previous_stack_length = len(stack)
        path.append((x,y))
        visited.add((x,y))
        if x == stop_x and y == stop_y:
            return path
        for next_x, next_y in surroundings(x,y):
            if next_x >= 0 and next_x < map.rows -1 and next_y >= 0 and next_y < map.cols -1:
                if map.map[next_x][next_y] == 0 and (next_x, next_y) not in visited:
                    stack.append((next_x, next_y))
        if len(stack) == previous_stack_length:
            path.pop()
    return path

rows = 4
cols = 4
start = set_fixed_location(rows,cols)
stop = set_fixed_location(rows,cols)


map = Map(rows, cols, start, stop)
# map.display_map()
# print(path_planning(map.start_location, map.stop_location, map))


my_fixed_map = [
    [0, 0, 0, 0],
    [0, 1, 1, 0],
    [1, 0, 1, 0],
    [0, 1, 1, 0]]
start = (0,0)
stop = (3,3)


def path_planning_on_fixed_Map(start, stop, map):
    start_x, start_y = start
    stop_x, stop_y = stop
    path = []
    stack = [(start_x, start_y)]
    visited = set()
    while stack:
        x, y = stack.pop()
        previous_stack_length = len(stack)
        path.append((x,y))
        visited.add((x,y))
        if x == stop_x and y == stop_y:
            return path
        for next_x, next_y in surroundings(x,y):
            if next_x >= 0 and next_x < len(map[0]) and next_y >= 0 and next_y < len(map) :
                if map[next_x][next_y] == 0 and (next_x, next_y) not in visited:
                    print(f"added {next_x, next_y}")
                    stack.append((next_x, next_y))
        if len(stack) == previous_stack_length:
            path.pop()
    return path
path_planning_on_fixed_Map(start, stop, my_fixed_map)