# import uiautomation
import os
import re

res = os.popen('ipconfig /all').read()
print(res)
res = re.findall(r"(?i).{0,200}?(.{2}-.{2}-.{2}-.{2}-.{2}-.{2}).{0,200}?ipv4.{0,200}?"
                 r"(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}).{0,200}?(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}).{0,200}?dns"
                 r".{0,200}?(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})", res, re.S)
print(res)
