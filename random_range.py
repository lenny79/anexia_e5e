from random import randrange

def rndrange(a, b):
  rnd_num = randrange(1, 7)
  returnstr = "Output: " + str(rnd_num) + " // First Argument: " + str(a) + " // Second Argument: " + str(b)
  return returnstr
