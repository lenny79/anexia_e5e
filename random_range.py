from random import randrange

def rndrange(a, b):
  rnd_num = randrange(1, 7)
  returnstr = "Out: " + str(rnd_num) + " // " + str(a) + str(b)
  return returnstr
