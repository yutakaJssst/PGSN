from pprint import pprint

from pgsn import *

# Define a custom subclass of Goal
CustomGoal = define_class("CustomGoal", goal_class,
                          record({"project": string("Alpha")}))

g = instantiate(CustomGoal, record({
    "description": string("Secure connection established"),
    "support": evidence(description="Verified by audit")
}))

pprint(prettify(g.fully_eval()))