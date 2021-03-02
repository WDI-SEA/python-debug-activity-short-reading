offense = False
defense = False
rule_changes = False

def get_offense(offense):  
  offense = True
  return offense

def get_defense(defense):  
  defense = True
  return defense

def get_rule_changes(rule_changes):
   rule_changes = True
   return rule_changes

offense = get_offense(offense)
defense = get_defense(defense)

if offense and defense:
   rule_changes = get_rule_changes(rule_changes)

print("How are the Jags doing?\n")
print("We have offense:", offense)
print("We have defense:", defense)
print("We have some rule changes:", rule_changes)

if offense and defense and rule_changes:
  print("We're going to the Super Bowl!")
else:
  print("I can't predict the future, but no, the Jaguars will never win the Super Bowl.")