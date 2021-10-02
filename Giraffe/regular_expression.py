import re

txt = "She often sends text messages on Friend ship"
if re.search('oftt|dss', txt):
    print("Matched")
else:
    print("Not matched")

