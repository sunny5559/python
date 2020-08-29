from datetime import date
import time
starttime = time.perf_counter()
ldates= []
d1 = date(2020,8,12)
d2 = date(2021,7,12)
d3 = date(2022,4,12)

ldates.append(d1)
ldates.append(d2)
ldates.append(d3)

ldates.sort()

time.sleep(4)
for d in ldates:
	print(d)

endtime = time.perf_counter()

print("execution time",endtime - starttime )