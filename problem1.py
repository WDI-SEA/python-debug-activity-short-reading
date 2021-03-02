offense = False
defense = False
rule_changes = False

def get_offense():
    offense = True
    return offense

def get_defense():
    defense = True
    return defense

def get_rule_changes():
    rule_changes = True
    return rule_changes

if offense and defense:
    get_rule_changes()

# get_offense()
# get_defense()

print("How are the Jags doing?\n")
print("We have offense:", get_offense())
print("We have defense:", get_defense())
print("We have some rule changes:", get_rule_changes())

if get_offense() and get_defense() and get_rule_changes():
    print("We're going to the Super Bowl!")
else:
    print("I can't predict the future, but no, the Jaguars will never win the Super Bowl.")