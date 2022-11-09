from random import randrange

def rndrange(a, b):
  rnd_num = randrange(1, 7)
  returnstr = "Output: " + str(rnd_num) + "\n First Argument: " + str(a) + "\n Second Argument: " + str(b)
  return returnstr
