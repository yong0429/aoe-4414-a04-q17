# ymdhms_to_jd.py
#
# Usage: python3 ymdhms_to_jd.py year month day hour minute second
#  Converts sez to ECEF vector components
# Parameters:
#  year: year in Gregorian
#  month: month in Gregorian
#  day: day in Gregorian
#  hour: hour in Gregorian
#  minute: minute in Gregorian
#  second: second in Gregorian
# Output:
#  Prints the Julian Date
#
# Written by Yonghwa Kim
# Other contributors: None

# import Python modules
import math # math module
import sys  # argv

# initialize script arguments
year = float('nan')
month = float('nan')
day = float('nan')
hour = float('nan')
minute = float('nan')
second = float('nan')

# parse script arguments
if len(sys.argv)==7:
  year = float(sys.argv[1])
  month = float(sys.argv[2])
  day = float(sys.argv[3])
  hour = float(sys.argv[4])
  minute = float(sys.argv[5])
  second = float(sys.argv[6])
else:
  print(\
   'Usage: '\
   'python3 ymdhms_to_jd.py year month day hour minute second'\
  )
  exit()

# Caculate Julian date for the given datetime
#jd = day-32075+1461*(year+4800+(month-14)/12)/4+367*(month-2-(month-14)/12*12)/12-3*((year+4900+(month-14)/12)/100)/4
jd = (day-32075+int(1461*(year+4800+int((month-14)/12))/4)+int(367*(month-2-int((month-14)/12)*12)/12)-int(3*int((year+4900+int((month-14)/12))/100)/4))

# JD at midnight
jd_midnight = jd - 0.5

# Fractional day part based on the time (hour, minute, second)
d_frac = (second + 60 * (minute + 60 * hour)) / 86400.0
    
# Final fractional Julian Date
jd_frac = jd_midnight + d_frac   
print(jd_frac)