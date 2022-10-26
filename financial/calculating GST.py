# The Program helps to calculate the net amount of a item when a certain percent of GST is applied.


def calculate(Original_price,GST_per):
    GST_amount=float(((GST_per*Original_price)/100))
    Price_wGST=Original_price+GST_amount
    print("Net Price after ",GST_per,"% GST is = ",Price_wGST)


calculate(100,25)

'''
Enter the original Price = 100
Enter the GST Percentage = 25
Price after  25.0 % GST is =  125.0

'''
