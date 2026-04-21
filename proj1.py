#complete your tasks in this file
import sys
import unittest
import math
from typing import *
from dataclasses import dataclass

sys.setrecursionlimit(10**6)


#Task 1
@dataclass(frozen=True)
class GlobeRect:
    lo_lat: float
    hi_lat: float
    west_long: float
    east_long: float

@dataclass(frozen=True)
class Region:
    rect: GlobeRect
    name: str
    terrain: str

@dataclass(frozen=True)
class RegionCondition:
    region: Region
    year: int
    pop: int
    ghg_rate: float


#Task 2
region_conditions = [RegionCondition(region = Region(rect = GlobeRect(lo_lat = 51.34,
                                                                    hi_lat = 51.68,
                                                                    west_long = -0.49,
                                                                    east_long = 0.09), 
                                                    name = "London",
                                                    terrain = "other"),
                                    year = 2019,
                                    pop = 14260000,
                                    ghg_rate = 454.8),
                RegionCondition(region = Region(rect = GlobeRect(lo_lat = -34.06,
                                                                hi_lat = -33.65,
                                                                west_long = 150.63,
                                                                east_long = 151.4), 
                                                name = "Sydney",
                                                terrain = "ocean"),
                                year = 2023,
                                pop = 5121000,
                                ghg_rate = 432.9),
                RegionCondition(region = Region(rect = GlobeRect(lo_lat = -28.93,
                                                                hi_lat = 33.13,
                                                                west_long = 152.96,
                                                                east_long = -136.37), 
                                                name = "Polynesia",
                                                terrain = "ocean"),
                                year = 2020,
                                pop = 688200,
                                ghg_rate = 81.3),
                RegionCondition(region = Region(rect = GlobeRect(lo_lat = 35.04,
                                                                hi_lat = 36.82,
                                                                west_long = -121.87,
                                                                east_long = -120.54), 
                                                name = "Central Coast",
                                                terrain = "mountain"),
                                year = 2025,
                                pop = 896613,
                                ghg_rate = 227)
]

#Task 3
#3.1
def emissions_per_capita(rc: RegionCondition) -> float:
    if rc.pop == 0:
        return 0.0
    return rc.ghg_rate/rc.pop

#3.2
def area(gr: GlobeRect) -> float:
    n = math.radians(gr.hi_lat)
    e =math.radians(gr.east_long)
    s = math.radians(gr.lo_lat)
    w = math.radians(gr.west_long)

    width = e - w
    if width <0:
        width += 2*math.pi

    return (6378.1**2) * abs((width)) * abs(math.sin(s)) - abs(math.sin(n))

#3.3
def emissions_per_square_km(rc: RegionCondition) -> float:
    return rc.ghg_rate/area(rc.region.rect)

#3.4
def pop_density(rc: RegionCondition) -> float:
    return rc.pop / area(rc.region.rect)

def densest(rc_list: list[RegionCondition]) -> RegionCondition:
   return densest_helper(rc_list, 1, rc_list[0].region.name, pop_density(rc_list[0]))

def densest_helper(rc_list: list[RegionCondition], idx: int, name: str, density: float) -> str:
    if idx == len(rc_list):
        return name
    
    dens = pop_density(rc_list[idx])

    if dens > density:
        return densest_helper(rc_list, idx +1, rc_list[idx].region.name, density)
    else:
        return densest_helper(rc_list, idx + 1, name, density)
    

#Task 4
def growth_rate(terrain: str) -> float:
    if terrain == "ocean":
        return 0.0001
    elif terrain == "mountains":
        return 0.0005
    elif terrain == "forest":
        return -0.00001
    else:
        return 0.0003
    
def project_condition(rc: RegionCondition, years: int) -> RegionCondition:
    rate = growth_rate(rc.region.terrain)

    pop_new = rc.pop * ((1+rate)** years)

    ghg_new = rc.ghg_rate *(pop_new/rc.pop)

    return RegionCondition(region = rc.region, year = rc.year + years, pop = int(pop_new), ghg_rate=ghg_new)

