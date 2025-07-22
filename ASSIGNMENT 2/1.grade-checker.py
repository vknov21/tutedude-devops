# Take a score as input and print the grade based on the following:
#   90+ : "A"
#   80-89 : "B"
#   70-79 : "C"
#   60-69 : "D"
#   Below 60 : "F"

score = int(input("Score: "))

# Using elif, the condition will only proceed when none of the previous condition gave True
if score >= 90:
    # This will get printed when the score is 90 or more than 90
    print("A")
elif score >= 80:
    # This will get printed only when the score is in between 80-90, and not when score is 90+ as previous condition was False
    print("B")
elif score >= 70:
    # This will get printed only when the score is in between 70-80, and not when score is 80+ as the previous conditions were False
    print("C")
elif score >= 60:
    # This will get printed only when the score is in between 60-70, and not when score is 70+ as the previous conditions were False
    print("D")
else:
    # This will get printed only when the score is in less than 60, and not when score is 70+ as the previous conditions were False
    print("F")
