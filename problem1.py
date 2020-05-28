offense = True
defense = True
rule_changes = True

def get_offense():
    offense = False

def get_defense():
    defense = False

def get_rule_changes():
    rule_changes = False

if offense and defense:
    get_rule_changes()

get_offense()

get_defense()

print("How are the Jags doing?\n")
print("We have offense:", offense)
print("We have defense:", defense)
print("We have some rule changes:", rule_changes)

if offense and defense and rule_changes:
  print("We're going to the Super Bowl!")
else:
  print("I can't predict the future, but no, the Jaguars will never win the Super Bowl.")