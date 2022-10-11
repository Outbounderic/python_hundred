import string


print("Welcome to the tip calculator.")
total_bill = int(input("What was the total bill? $"))
tip_prct = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
total_ppl = int(input("How many people to split the bill between? "))

indv_bill = (total_bill + (total_bill * (tip_prct / 100))) / total_ppl

print(f"Each person should pay: ${str(indv_bill)}")
