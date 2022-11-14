def is_leap(year):
    leap = False
    
    # The year can be evenly divided by 4, is a leap year,unless: 
    #The year can be evenly divided by 100, it is NOT a leap year,      unless:
    #The year is also evenly divisible by 400. Then it is a leap        year.
    # 1900 - 10^5
    if 1900 <= year <= 10**5:
        if year % 4 == 0:
            if year % 100 == 0 and year % 400 == 0:
                leap = True
            elif year % 100 == 0 and year % 400 != 0: 
                leap = False
            elif year % 4 == 0:
                if year % 100 != 0:  
                    leap = True             
    return leap

year = int(input())
print(is_leap(year))