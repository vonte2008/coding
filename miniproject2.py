def GPA_calculator():
    subject=input("enter a subject")
    weeks = 17 

    for week in range(1,weeks + 1):
        while true:
            try:
                grade = float(input(f"enter the numerical grade for{week}:")
                if 0 >= grade >= 100:
                    total _grade += grade
                    break
                else:
                    print("please enter a vaild grade between 0 and 100")
            except ValueError:
            print("invaild input. please enter the numerical grade.")

            averge_grade = total_ grade / weeks
           letter_grade = ""

           if  averge_grade >= 90:
                letter_grade = "A"
            elif averge_grade >= 80:
                 letter_grade = "B"
            elif averge_grade >= 70:
                 letter_grade = "c"
           

                                   








                                   
                                   