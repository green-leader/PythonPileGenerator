# Sion Fandrick
import random
import time  # For seeding the random

pile = []

while 1:
  data = raw_input("What are the options? ")
  if( data != "" ):
    pile.append(data)
  else:
    break


# Print random selection from pile
print "Choice: " +  pile[random.randint(0, len(pile))]
