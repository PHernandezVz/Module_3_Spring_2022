"""
Program: if_elif_statement_assignment.py
Author: Patricia Hernandez-Vasquez
Last date modified: 02/14/2022
The purpose of this program is to show a user the different prices for a subscription box using if_elif statements.
For each tier, or input, the output should reveal the monthly cost.
"""

#Print some details to the screen
    #talk about the Prog Toolkit Month
    #talk about what it could include
    #list out the levels
    #please select a level to hear the price
#Get some sort of input from the user

#figure which level the user selected; the hw wants us to use an if statement
    #if the user selected platinum then print 'the cost is $60'
    #if the user selected gold then print 'the cost is $10'
    #...

print('Thank you for your interest in our Programmer\'s Toolkit Monthly Subscription Box!')
print('Our subscription box offers members a variety of t-shirts, stickers, figurines, and even programming books each month.')
print('We offer four different subscription tiers: Platinum, Gold, Silver, and Bronze.')
print('Not ready for the commitment? Feel free to try our free trial!')
tier = input('Select a level to view our prices: ')

if tier == 'Platinum':
    print('Our Platinum tier costs $60 per month.')
elif tier == 'Gold':
    print('Our Gold tier costs $45 per month.')
elif tier == 'Silver':
    print('Our Silver tier costs $30 per month.')
elif tier == 'Bronze':
    print('Our Bronze tier costs $10 per month.')
elif tier == 'Free Trial':
    print('Our Free Trial costs $0 per month for the first two months. After the two months, you will be prompted to choose another tier.')

# Input:        Expected Output:                            Actual Output:
# Platinum      Our Platinum tier costs $60 per month.      Our Platinum tier costs $60 per month.
# Gold          Our Gold tier costs $45 per month.          Our Gold tier costs $45 per month.
# Silver        Our Silver tier costs $30 per month.        Our Silver tier costs $30 per month.
# Bronze        Our Bronze tier costs $10 per month.        Our Bronze tier costs $10 per month.
# Free Trial    Our Free Trial costs $0 per month           Our Free Trial costs $0 per month for the first two months.
#               for the first two months.                   After the two months, you will be prompted to choose another tier.
#               After the two months, you will be
#               prompted to choose another tier.
