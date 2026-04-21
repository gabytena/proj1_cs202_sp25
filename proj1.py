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
    name: "string"
    terrain: "string"

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
        width += 2+math.pi

    return (6378.1**2) * abs(width) * math.sin(s) - math.sin(n)