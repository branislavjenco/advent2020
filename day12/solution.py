from utils import file_into_list
import re


def parse(instruction):
    match = re.match("^([A-Z])(\d+)$", instruction)
    if not match:
        raise AssertionError("foobar")
    return match.group(1), int(match.group(2))


instructions = [parse(i) for i in file_into_list("day12/input.txt")]


class State:
    def __init__(self, pos, rot):
        self.pos = pos
        self.rot = rot

    def manhattan(self):
        return abs(self.pos[0]) + abs(self.pos[1])
    
    def __str__(self):
        return f"Pos: {self.pos}, Rot: {self.rot}"

# rot 0 is east, 90 is north, 180 is west, 270 is south

def part_1():
    def north(value, state):
        state.pos[1] += value

    def south(value, state):
        state.pos[1] -= value

    def east(value, state):
        state.pos[0] += value

    def west(value, state):
        state.pos[0] -= value

    def left(value, state):
        new_rot = (state.rot + value) % 360
        state.rot = new_rot

    def right(value, state):
        new_rot = (state.rot - value) % 360
        state.rot = new_rot

    def forward(value, state):
        if state.rot == 0:
            east(value, state)
        elif state.rot == 90:
            north(value, state)
        elif state.rot == 180:
            west(value, state)
        elif state.rot == 270:
            south(value, state)


    state = State([0, 0], 0)
    for action, value in instructions:
        if action == 'N':
            north(value, state)
        elif action == 'S':
            south(value, state)
        elif action == 'E':
            east(value, state)
        elif action == 'W':
            west(value, state)
        elif action == 'L':
            left(value, state)
        elif action == 'R':
            right(value, state)
        elif action == 'F':
            forward(value, state)
    print(state.manhattan())
        

def part_2():
    # in part 2, the ship rotation doesn't come into play
    ship_state = State([0, 0], 0)
    # waypoint's pos is relative to ship, rotation is ignored 
    waypoint_state = State([10, 1], 0)

    def north(value, ship, waypoint):
        waypoint.pos[1] += value

    def south(value, ship, waypoint):
        waypoint.pos[1] -= value

    def east(value, ship, waypoint):
        waypoint.pos[0] += value

    def west(value, ship, waypoint):
        waypoint.pos[0] -= value

    def rotate(value, waypoint):
        if value == 90:
            new_pos = [-waypoint.pos[1], waypoint.pos[0]]
            waypoint.pos = new_pos
        elif value == 180:
            new_pos = [-waypoint.pos[0], -waypoint.pos[1]]
            waypoint.pos = new_pos
        elif value == 270:
            new_pos = [waypoint.pos[1], -waypoint.pos[0]]
            waypoint.pos = new_pos

    def left(value, ship, waypoint):
        rot = value % 360
        rotate(rot, waypoint)
        
    def right(value, ship, waypoint):
        rot = -value % 360
        rotate(rot, waypoint)

    def forward(value, ship, waypoint):
        ship.pos = [ship.pos[0] + waypoint.pos[0] * value, ship.pos[1] + waypoint.pos[1] * value]
        
        
    for action, value in instructions:
        print(action, value)
        if action == 'N':
            north(value, ship_state, waypoint_state)
        elif action == 'S':
            south(value, ship_state, waypoint_state)
        elif action == 'E':
            east(value, ship_state, waypoint_state)
        elif action == 'W':
            west(value, ship_state, waypoint_state)
        elif action == 'L':
            left(value, ship_state, waypoint_state)
        elif action == 'R':
            right(value, ship_state, waypoint_state)
        elif action == 'F':
            forward(value, ship_state, waypoint_state)

    print(ship_state.manhattan())

part_2()
