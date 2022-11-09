from random import randrange

def rndrange(event, context):
  rnd_num = 0
  
  try:
    a, b = event['data']['a'], event['data']['b']
    rnd_num = randrange(a, b)
  
  except Exception:
    a, b = 0, 0
      
  returnstr = "Output: " + str(rnd_num) + " / First Argument: " + str(event) + " / Second Argument: " + str(context)
  return returnstr
