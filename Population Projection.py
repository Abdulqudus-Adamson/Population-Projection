#   This population projection is based on the following assumptions:
# One birth every 7 seconds.
# One death every 13 seconds.
# One new immigrant every 45 seconds.

# This programme was created to give the birth rate , death rate , immigrant rate and population after a year and 5 years later.


current_Population = input("Enter the amount of the current population: ")

birth_Rate = (31536000 // 7)
death_Rate = (31536000 // 13)
immigrant_Rate = (31536000 // 45)

print("The amount of babies given birth to was approximately ", birth_Rate)
print("The amount of death registered approximately was approximately ", death_Rate)
print("The amount of immigrant that came into the country was approximately ", immigrant_Rate)

#This prints out the projected birth_Rate, death_Rate and immigration rate after a year already calculated along with the strings(sentences).

def populationAtTheEndOfTheYear(birth_Rate, death_Rate, immigrant_Rate) : # This function takes in 3 parameters.
    return (current_Population + (birth_Rate + immigrant_Rate)) - death_Rate   # This returns the value of the expression which comes after the return keyword.


result1 = populationAtTheEndOfTheYear(birth_Rate, death_Rate, immigrant_Rate)
print("The projected population after a year is ", result1) #This prints out the projected population after a year.

print()
print()                          #whitespaces
print()


birthRateAfter5Years = (31536000 // 7) * 5
deathRateAfter5Years = (31536000 // 13) * 5
immigrantRateAfter5Years = (31536000 // 45) * 5

print("After 5 Years, The amount of babies given birth to is approximately ", birthRateAfter5Years)
print("After 5 Years, The amount of peoople that kicked the bucket is approximately ", deathRateAfter5Years)
print("After 5 Years, The amount of immigrant that came into the country is approximately ", immigrantRateAfter5Years)

#This prints out the projected birth_Rate, death_Rate and immigration rate after 5 Years already calculated along with the strings(sentences).


def populationAfter5Years(birthRateAfter5Years,deathRateAfter5Years, immigrantRateAfter5Years) :
    return (current_Population + (birthRateAfter5Years + immigrantRateAfter5Years)) - deathRateAfter5Years

result2 = populationAfter5Years(birthRateAfter5Years,deathRateAfter5Years, immigrantRateAfter5Years)
print("The projected population after 5 Years will be ", result2)  #This prints out the projected population after 5 Years.
















