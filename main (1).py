1.2#Leap year
#Leapyear

""""
year%4==0&
year%100=0/
year%400==0

"""
def isleapYear(year):
  if (year%4 == 0 and year%100 != 0) or (year%400 == 0) :
    return True
  else:
    return False

year=int(input("Enter a year:"))

if isleapYear(year):
  print('{} is a leap year.'.format(year))
else:
  print('{}is not a leap year.'.format(year))
