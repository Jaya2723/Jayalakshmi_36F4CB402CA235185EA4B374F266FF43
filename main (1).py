# Leap year or not

def isleapYear(year):
  if(year%4==0 and year%10!=0) or year%400==0:
     return True 
  else:
    return False 
year=2024
if isleapYear(year):
  print('{}is a Leapyear.'.format(year))
else:
  print('{}is not a Leapyear.'.format (year))
  