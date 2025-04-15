from pprint import pprint

from pgsn.gsn_term import *

requirements = list_term((
    string("Firewall enabled"),
    string("Encrypted communication"),
    string("Access control active")
))

goal_template = lambda_abs(variable("desc"),
    goal(description=variable("desc"),
         support=evidence(description=variable("desc")))
)

goals = map_term(goal_template, requirements)

secure_goal = goal(
    description=string("Security requirements fulfilled"),
    support=immediate(goals)
)

pprint(prettify(secure_goal.fully_eval()))
