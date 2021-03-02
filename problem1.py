offense = True
defense = True
rule_changes = True

def get_offense():
#   offense = True
  return offense
  

def get_defense():
#   defense = True
  return defense
  

def get_rule_changes():
    # rule_changes = True
    return rule_changes

if offense and defense:
    get_rule_changes()

get_offense()
# print('offense is', offense)
get_defense()
# print('defense is', defense)

print("How are the Jags doing?\n")
print("We have offense:", offense)
print("We have defense:", defense)
print("We have some rule changes:", rule_changes)

if offense and defense and rule_changes:
  print("We're going to the Super Bowl!")
else:
  print("I can't predict the future, but no, the Jaguars will never win the Super Bowl.")