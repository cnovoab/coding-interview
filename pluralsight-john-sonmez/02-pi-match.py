# Pi Match
# --------------------------------------------------------------------------
# A Pi Match score is defined by how close the digits in a number are to the
# approximation of Pi, 3.14.
#
# In order to calculate the Pi Match score for a number, we drop the decimal from the
# Pi approximation, leaving us with 314 and we start from the leftmost digits of the
# number and calculate the difference between those three digits and 314.
#
# We keep shifting over one digit to the right and performing the same calculation
# until we do not have 3 digits left in our number. The total score is the average of
# each 3 digit score. If a number has less than 3 digits it should have a score of 0.
#
# You can assume that the number will have at most 12 digits.
#
# - Example 1: For the number 3149 the Pi Match score is calculated as follows
# (314 - 314 = 0) + (149 - 314 = -165) / 2 = -82.5
#
# - Example 2: For the number 357878 the Pi Match score is calculated as follows
# (357 - 314 = 43) + (578 - 314 = 264) + (787 - 314 = 473) + (878 - 314 = 564) / 4 =
# 336


