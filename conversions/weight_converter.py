weight = int(input("enter your weight:"))
lb_or_kg = input("lb or kg:")
converted_weight = ""
if lb_or_kg =="lb":
    converted_weight = weight / 2.205 + "kgs"
else:
    converted_weight = weight * 2.205 + "lbs"



