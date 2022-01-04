#What is score
score = int(input("What is the student's score?"))
#nested loop to determine letter grades
#>= 90 for A
if score >= 90:
    print("Letter Grade: A")
#>= 80 for B
else:
    if score >= 80:
        print("Letter Grade: B")
    else:
        if score >= 70:
            print("Letter Grade: C")
        else:
            if score >= 60:
                print("Letter Grade: D")
            else:
                print("Letter Grade: E")
