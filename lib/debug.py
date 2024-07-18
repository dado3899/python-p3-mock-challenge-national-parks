#!/usr/bin/env python3
import ipdb

from classes.many_to_many import NationalPark
from classes.many_to_many import Visitor
from classes.many_to_many import Trip

if __name__ == '__main__':
    v1 = Visitor(name = "Bob")
    v2 = Visitor(name = "Grey")
    # v1.name = "New Visitor"
    # print(v1.name)

    p1 = NationalPark(name="Rocky Mountains")
    p2 = NationalPark(name="Yosemite")
    # p1.name = "new park"

    Trip(
        visitor=v1,
        national_park=p1,
        start_date="May 1st",
        end_date="May 2nd"
    )
    Trip(
        visitor=v1,
        national_park=p1,
        start_date="May 5st",
        end_date="May 7nd"
    )
    Trip(
        visitor=v2,
        national_park=p1,
        start_date="May 5st",
        end_date="May 7nd"
    )
    Trip(
        visitor=v1,
        national_park=p2,
        start_date="May 5st",
        end_date="May 7nd"
    )

    print(v2.total_visits_at_park(p2))
    