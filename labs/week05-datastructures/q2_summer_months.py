# Q2: Tuple of months and summer months
# Author: Sophie

months = (
    "January", "February", "March", "April", "May",
    "June", "July", "August", "September",
    "October", "November", "December"
)

# Summer months (May, June, July) are indexes 4, 5, 6
summer = months[4:7]

for month in summer:
    print(month)