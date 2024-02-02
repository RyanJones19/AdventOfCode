from __future__ import annotations
from copy import deepcopy
import sys
import re
import time

valve_data = open(sys.argv[1]).read().strip().split('\n')

source_valve_re = re.compile(r"Valve ([A-Z]{2})")
target_valves_re = re.compile(r"valve(?:s?)* (([A-Z]{2}, )*[A-Z]{2})")
flow_rate_re = re.compile(r"rate=(\d+)")

class Volcano:
    def __init__(self, valves: list[Valve]):
        self.valves = valves
        self.time_to_explode = 30
        self.pressure_released = 0
        self.previous_pressure = 0
        self.previous_valve = None
        self.current_valve = None
        self.previous_open_valves = []
        self.open_valves = []
        self.max_pressure = 0
    
    def travel_to_valve(self, valve: Valve):
        print(f"Traveling to valve {valve.valve_name} from {self.current_valve.valve_name}")
        self.tick(valve, True)
        valve.visited = True
        self.previous_valve = self.current_valve
        self.current_valve = valve

    def is_valid_move(self, valve: Valve):
        print(f"Checking for valid move from {self.current_valve.valve_name} to {valve.valve_name}")
        return not valve.visited

    def turn_valve(self, valve: Valve):
        print(f"Turning Valve {self.current_valve.valve_name} with flow rate {self.current_valve.flow_rate} the valve open status is {self.current_valve.is_open}")
        print(f"The volcanoes open valves are {[valve.valve_name for valve in self.open_valves]}")
        self.tick(valve, False)
        #if valve.turn():
        #    self.open_valves.append(valve)

    def tick(self, valve: Valve, is_movement: bool):
        print()
        print(f"=========== CURRENT MINUTE: {self.time_to_explode} =================")
        print(f"Ticking {'MOVEMENT' if is_movement else 'VALVE TURN'}")
        self.time_to_explode -= 1
        self.previous_pressure = self.pressure_released
        self.pressure_released += self.calculate_pressure()
        if not is_movement:
            print(f"1: previous open valves is now: {[valve.valve_name for valve in self.previous_open_valves]}")
            cloned_valves = deepcopy(self.open_valves)
            self.previous_open_valves = cloned_valves
            print(f"2: previous open valves is now: {[valve.valve_name for valve in self.previous_open_valves]}")
            if valve.turn():
                print(f"Added a new open valve: {[valve.valve_name for valve in self.open_valves]} previous open valves is now: {[valve.valve_name for valve in self.previous_open_valves]}")
                self.open_valves.append(valve)
                print(f"Added a new open valve: {[valve.valve_name for valve in self.open_valves]} previous open valves is now: {[valve.valve_name for valve in self.previous_open_valves]}")
        #self.previous_pressure = self.pressure_released
        #self.pressure_released += self.calculate_pressure()
        #print(f"After ticking the pressure released is {self.pressure_released}")
        #print()

    def untick(self, is_movement: bool):
        print()
        print(f"=========== CURRENT MINUTE: {self.time_to_explode} =================")
        print(f"Unticking {'MOVEMENT' if is_movement else 'VALVE TURN'}")
        self.time_to_explode += 1
        if is_movement:
            self.current_valve = self.previous_valve
        else:
            self.open_valves = self.previous_open_valves
        #self.open_valves = self.previous_open_valves
        self.pressure_released = self.previous_pressure
        #self.current_valve = self.previous_valve
        print(f"After unticking new time is {self.time_to_explode} new open valves = {[valve.valve_name for valve in self.open_valves]} pressure_released is {self.pressure_released} current valve is now {self.current_valve.valve_name}")
        #print()

    def calculate_pressure(self):
        #print("Calculating pressure")
        additional_pressure = 0
        for valve in self.open_valves:
            additional_pressure += valve.flow_rate
        #print(f"Calculated pressure and returning {additional_pressure}")
        return additional_pressure

    def traverse(self):
        #time.sleep(1)
        #print()
        print(f"Current Volcano Time Left: {self.time_to_explode} with Total Released Pressure: {self.pressure_released}")
        if self.time_to_explode == 0:
            print("Volcano Exploded after a movement")
            self.max_pressure = max(self.max_pressure, self.pressure_released)
            return
        else:
            print(f"Volcano still active for {volcano.time_to_explode} seconds")
            print(f"Current valve is {self.current_valve.valve_name} with flow rate {self.current_valve.flow_rate}")
            if (not self.current_valve.is_open) and self.current_valve.flow_rate != 0:
                self.turn_valve(self.current_valve)
                if self.time_to_explode == 0:
                    print("Volcano Exploded after a valve opening")
                    self.max_pressure = max(self.max_pressure, self.pressure_released)
                    return
            canMove = False
            for valve in self.current_valve.target_valves:
                if not valve.visited:
                    canMove = True
                    break
            if canMove:
                for valve in self.current_valve.target_valves:
                    if valve.visited:
                        continue
                    if self.is_valid_move(valve):
                        current_time_to_explode = self.time_to_explode
                        print(f"Before moving the time to explode was {current_time_to_explode}")
                        self.travel_to_valve(valve)
                        self.traverse()
                        print(f"After returning from recursive call time to explode was {current_time_to_explode}")
                        volcano.untick(True)
                        valve.visited = False
                    else: 
                        print(f"After returning from recursive call time to explode was {current_time_to_explode}")
                        valve.visited = False
                        volcano.untick(False)
            else:
                while self.time_to_explode > 0:
                    print("Cant move anywhere, will let volcano explode")
                    volcano.tick(valve, True)

class Valve:
    def __init__(self, valve_name: str, flow_rate: int, target_valves: list[Valve]):
        self.valve_name = valve_name
        self.flow_rate = flow_rate
        self.target_valves = target_valves
        self.is_open = False
        self.visited = False

    def turn(self) -> bool:
        self.is_open = False if self.is_open else True
        print(f"Turning valve {self.valve_name} and is open is now {self.is_open}")
        return self.is_open

volcano = Volcano([])

for line in valve_data:
    source_valve = source_valve_re.search(line).group(1)
    flow_rate = int(flow_rate_re.search(line).group(1))
    new_valve = Valve(source_valve, flow_rate, [])
    volcano.valves.append(new_valve)

for line in valve_data:
    source_valve = source_valve_re.search(line).group(1)
    target_valves = target_valves_re.search(line).group(1).split(',')
    target_valves = [target.strip() for target in target_valves]

    for outer_valve in volcano.valves:
        if outer_valve.valve_name == source_valve:
            for inner_valve in volcano.valves:
                if inner_valve.valve_name in target_valves:
                    outer_valve.target_valves.append(inner_valve)
    


#valve1 = Valve('AA', 10, [])
#valve2 = Valve('BB', 15, [])
#valve3 = Valve('CC', 25, [])
#valve4 = Valve('DD', 12, [])

#valve1.target_valves = [valve2, valve3, valve4]
#valve2.target_valves = [valve1, valve3, valve4]
#valve3.target_valves = [valve1, valve2, valve4]
#valve4.target_valves = [valve1, valve2, valve3]

#volcano.current_valve = valve1
#volcano.current_valve.visited = True

#for valve in volcano.current_valve.target_valves:
#    time.sleep(3)
#    if volcano.is_valid_move(valve):
#        volcano.travel_to_valve(valve)
#        volcano.turn_valve(valve)

#volcano.untick(True)
#volcano.untick(True)

volcano.current_valve = volcano.valves[0]
volcano.current_valve.visited = True
volcano.traverse()
print(volcano.max_pressure)


