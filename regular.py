
  正则表达式使用汇总：
 import re
 # 4到16位（字母，数字，下划线，减号）
 if re.match(r'^[a-zA-Z0-9_-]{4,16}$', "abwc"):
    print("匹配")
 #正整数正则
 if re.match(r'^\d+$',"42"):
    print("匹配")

 #负整数正则
 if re.match(r'^-\d+$',"42"):
    print("匹配")
#整数正则
if re.match(r'^-?\d+$',"-42"):
    print("匹配")
                                
