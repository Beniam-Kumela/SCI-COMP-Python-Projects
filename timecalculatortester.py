def add_time(start, duration, day = '1'):
  starthours = start.split(':')[0]
  startminutes = start.split(':')[1].split()[0]
  meridian = start.split(':')[1].split()[1]
  durationhours = duration.split(':')[0]
  durationminutes = duration.split(':')[1]
  totalhours = int(starthours) + int(durationhours)
  totalminutes = int(startminutes) + int(durationminutes)
  global daydisplay
  global dayselasped
  if totalminutes > 59:
      totalminutes = totalminutes - 60
      totalhours = totalhours + 1
  if totalminutes < 10:
      totalminutes = '0' + str(totalminutes)
  if totalhours < 12:
    daydisplay = None
  if totalhours == 12:
    if meridian == 'AM':
      meridian = 'PM'
      daydisplay = None
    else:
      meridian = 'AM'
      daydisplay = ' (next day)'
  if 12 < totalhours <= 24:
    totalhours = totalhours - 12
    if meridian == 'AM':
      meridian = 'PM'
      daydisplay = None
    else:
      meridian = 'AM'
      daydisplay = ' (next day)'
  if totalhours > 24:
    dayselasped = totalhours // 24
    totalhours = totalhours % 24
    if dayselasped == 1:
      if totalhours >= 12:
        if meridian == 'AM':
          meridian = 'PM'
          daydisplay = ' (next day)'
        else:
          meridian = 'AM'
          daydisplay = ' (2 days later)'
      else:
        daydisplay = ' (next day)'
    else:
      if totalhours > 12:
        totalhours = totalhours - 12
        if meridian == 'AM':
          meridian = 'PM'
          daydisplay = ' (' + str(dayselasped) + ' days later)'
        else:
          meridian = 'AM'
          daydisplay = ' (' + str(dayselasped + 1) + ' days later)'
      else:
        daydisplay = ' (' + str(dayselasped) + ' days later)'
  if day != '1':
    lday = day.lower()
    week = list()
    week.append('monday')
    week.append('tuesday')
    week.append('wednesday')
    week.append('thursday')
    week.append('friday')
    week.append('saturday')
    week.append('sunday')
    weekindex = week.index(lday)
    try:
      if daydisplay == None:
        pday = lday
      if daydisplay == ' (next day)':
        pday = week[weekindex + 1]
      else:
        try:
          pday = week[dayselasped + weekindex + 1]
        except:
          pday = week[(dayselasped % 7) + weekindex + 1]
    except:
      nweek = week[::-1]
      nweekindex = nweek.index(lday)
      if daydisplay == ' (next day)':
        pday = nweek[nweekindex - 1]
      else:
        try:
          pday = nweek[nweekindex - dayselasped - 1]
        except:
          pday = nweek[nweekindex - (dayselasped % 7) - 1]
    if daydisplay == None:
        new_time = str(totalhours) + ':' + str(totalminutes) + ' ' + meridian + ', ' + pday.capitalize()
    else:
        new_time = str(totalhours) + ':' + str(totalminutes) + ' ' + meridian + ', ' + pday.capitalize() + daydisplay
  else:
    if daydisplay == None:
        new_time = str(totalhours) + ':' + str(totalminutes) + ' ' + meridian
    else:
        new_time = str(totalhours) + ':' + str(totalminutes) + ' ' + meridian + daydisplay
  return new_time

print(add_time("3:30 PM", "2:12", "Monday"))
