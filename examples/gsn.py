from pprint import pprint

from pgsn import *

g = goal(
    description=string("System is secure"),
    support=strategy(
        description=string("Break into sub-goals"),
        sub_goals=[
            goal(description="Input validated",
                 support=evidence(description="Static analysis passed")),
            goal(description="Output sanitized",
                 support=evidence(description="Fuzzing test succeeded"))
        ]
    )
)

pprint(prettify(g.fully_eval()))