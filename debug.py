offense = False
defense = False
rule_changes = False

def get_offense():
  global offense  
  offense = True
  print(offense)

def get_defense():
  global defense  
  defense = True
  print(defense)

  def get_rule_changes():
    global rule_changes  
    rule_changes = True
    print(rule_changes)

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


  #Global variables 
    #variables that are created outside of a function ; can be used by everyone, both inside of functions and outside
  #Global keywards
    #they allow you to change the global variable within a function; use the global keyword if you want to change a global variable inside a function