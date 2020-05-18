#!/usr/bin/env python
# coding: utf-8

# In[14]:


import csv


# In[15]:


from datetime import datetime


# In[16]:


start = input('Enter Starting Date and Time (i.e 15/05/2020 11:30): ')
stop = input('Enter Stoping Date and Time (i.e 16/05/2020 1:30): ')

#conversion
objstart = datetime.strptime(start, '%d/%m/%Y %H:%M')
objstop = datetime.strptime(stop, '%d/%m/%Y %H:%M')
diff = (objstop - objstart).total_seconds()/3600

date1 = str(objstart.date())
date2 = str(objstop.date())
time1 = str(objstart.time())
time2 = str(objstop.time())

'''
print(date1)
print(date2)
print(time1)
print(time2)
'''
# $2.5 per hour
pay_rate = 5
amount = str(diff * pay_rate)
row = ['Start Date', 'Start Time', 'Stop Date', 'Stop Time', 'Total Hours', 'Amount Earned']
data = [[date1, time1, date2, time2, diff, amount]]

with open('time.csv', 'a+', newline='\n', encoding='utf8') as f:
	f.seek(0)
	#Check if the file is empty
	file_data = f.read(100)
	if len(file_data) > 0:
		writer = csv.writer(f) 
		writer.writerows(data)
	else:
		writer = csv.writer(f)
		writer.writerow(row)
		writer.writerows(data)
	

print('Total amount earned: $' + amount)


# In[ ]:




