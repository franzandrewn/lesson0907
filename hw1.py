# Функция, принимающая номер или название месяца - возвращающая что за время года в строке
def getSeason(month):
  if month == 1 or month == 'Январь':
    return 'Зима'
  elif month == 2 or month == 'Февраль':
    return 'Зима'
  elif month == 3 or month == 'Март':
    return 'Весна'

def getSeasonAlt(month):
  if str(type(month))=='str' and month.isdigit()==True:
    month = int(month)
  if month in [12,1,2, 'Декабрь', 'Январь', 'Февраль']:
    return 'Зима'
  elif month in [3,4,5,'Март', 'Апрель', 'Май']:
    return 'Весна'
  elif month in [6,7,8,'Июнь', 'Июль', 'Август']:
    return 'Лето'
  elif month in [9,10,11,'Сентябрь', 'Октябрь', 'Ноябрь']:
    return 'Осень'

def getSeasonAltAlt(month):
  monthToSeason = {'12':'Зима', '1':'Зима', '4':'Осень'}
  return monthToSeason[month]

print(getSeasonAlt(input()))
print(getSeasonAlt(4))
print(getSeasonAlt('Март'))

print(getSeasonAltAlt['12'])
