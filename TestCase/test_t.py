"""
i=0
while i < 5 :
    # input_1.send_keys(shuijisu)
    i += 1
    print(i)
else:
    print('结束')
s = 'ab,cde,fgh,ijk'
s=s.split(',')
print(s[-1])


import os

activity = os.system('adb shell dumpsys activity | findstr "mFocusedActivity"')
print(activity)

assert (1 == 0)
"""
from Utils.getyaml import yl

print(yl['test_buy']['course_ac'])

