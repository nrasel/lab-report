import calendar


def print_months_of_year(year):
    print(f"Months of the year {year} with the number of days:")
    
    for month in range(1, 13): 
        month_name = calendar.month_name[month]  
        print(f"{month_name}")


year = int(input("Enter a year: "))
print_months_of_year(year)