from calendar import weekday 
print sum(1 for year in range(1901,2001) for month in range(1,13) if weekday(year,month,1) == 6)
