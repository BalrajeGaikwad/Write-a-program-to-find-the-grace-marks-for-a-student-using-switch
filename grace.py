#Write a program to find the grace marks for a student using switch. The user should enter the class obtained by the student and the number of subjects he has failed in. 
# Use the following logic:

#1) If the student gets first class and the number of subjects he failed in is greater than 3, 
#   then he does not get any grace. Otherwise the grace is of 5 marks per subject.

#2) If the student gets second class and the number of subjects he failed in is greater than 2, 
#   then he does not get any grace. Otherwise the grace is of 4 marks per subject.

#3) If the student gets third class and the number of subjects he failed in is greater than 1, 
#   then he does not get any grace. Otherwise the grace is of 5 marks.


while True:
    
    print("1. First")
    print("2. second")
    print("3. third")
    print("Choose one of them ")
    class_std=int(input("Enter the class of student"))

    if class_std==1:
        failed=int(input("how many subject student failed :-"))
        if(failed>3):
            print("Does not get any grace")
        else:
            print("The grace is 5 marks per subject")
    elif class_std==2:
        failed=int(input("how many subject student failed :-"))
        if(failed>2):
            print("Does not get any grace")
        else:
            print("The grace is 4 marks per subject")
    elif class_std==3:
        failed=int(input("how many subject student failed :-"))
        if(failed>1):
            print("Does not get any grace")
        else:
            print("The grace is 5 marks per subject")

    else:
        break



    

    



