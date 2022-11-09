from random import randrange

def rndrange(event, context):
  try:
      a, b = event['data']['a'], event['data']['b']
  except Exception:
        a, b = 0, 0
  
  rnd_num = randrange(a, b)
  returnstr = "Output: " + str(rnd_num) + " // First Argument: " + str(a) + " // Second Argument: " + str(b)
  return returnstr
