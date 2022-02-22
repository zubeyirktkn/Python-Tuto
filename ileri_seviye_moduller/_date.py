from datetime import datetime, time, timedelta
"""
from datetime import date
from datetime import time
import datetime
"""
simdi=datetime.now()#simdinin bilgileri-----------------------
"""
result=simdi.month
result=simdi.year
result=datetime.ctime(simdi)
result=datetime.strftime(simdi,"%Y")
result=datetime.strftime(simdi,"%A")
result=datetime.strftime(simdi,"%Y %A %B")
"""
"""
t="21 Nisan 2021"
gun,ay,yil=t.split()#boşluktan ayırır
print(gun)
print(ay)
print(yil)
"""
"""
t="15 April 2019 hour 13:08:40"
result = datetime.strptime(t,"%d %B %Y hour %H:%M:%S")

result=datetime.timestamp(birthday)#saniye
result=datetime.fromtimestamp(result)#saniye to datetime
result = datetime.fromtimestamp(0)
"""
birthday=datetime(1999,5,3,3,15,00)#dogum günü bilgilerim-----
print(birthday)
print(simdi)
#result=simdi-birthday#timedelta
#result=result.days
#result=result.seconds#saniyeler arası farkı veriyor ogünden bugüne kaç saniye geçti vermiyor!

result=simdi+timedelta(days=10)
result=simdi-timedelta(days=10)
print(result)
