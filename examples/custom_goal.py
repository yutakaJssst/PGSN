from pprint import pprint

from pgsn import *

# Define a custom subclass of Goal
CustomGoal = define_class("CustomGoal", goal_class, project="Alpha")

g = instantiate(CustomGoal, description="Secure connection established",
    support=evidence(description="Verified by audit"))

pprint(prettify(g.fully_eval()))