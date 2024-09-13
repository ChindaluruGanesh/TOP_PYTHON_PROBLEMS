principal = int(input('Enter amount : '))
rate_of_interest = int(input('Enter rate of interest : '))
years = int(input('Enter no of years : '))

#Simple Interest --> PNR / 100
# / --> float value 
# // --> int value

simple_interest = (principal * years * rate_of_interest) // 100
print(simple_interest)
