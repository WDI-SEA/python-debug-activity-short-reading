offense = False
defense = False
rule_changes = False

print("How are the Jags doing?\n")
def get_offense():
  offense = True
  print("We have offense:", offense)
  return offense
  

def get_defense():
  defense = True
  print("We have defense:", defense)
  return defense

def get_rule_changes():
    rule_changes = True
    print("We have some rule changes:", rule_changes)
    if offense and defense:
                print('111', offense)
                get_rule_changes()
    return rule_changes



def team_win():
    if offense and defense and rule_changes:
        print("We're going to the Super Bowl!")
    else:
        print(offense)
        print("I can't predict the future, but no, the Jaguars will never win the Super Bowl.")

get_offense()
get_defense()
get_rule_changes()
team_win()