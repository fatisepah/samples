import random
import numpy as np

DicOfSentenses={
"Lesson 1":"",
"I'm crazy about you!":"دیونتم","Don't change the subject!":"بحث رو عوض نکن","I don't blame you!":"سرزنشت نمی کنم",
"Butt out!":"دخالت نکن","Stay out of it!":"دخالت نکن","Have courage!":"شجاع باش",
"Curiosity killed the cat!":"کنجکاوری کار دستت میده","Help yourself!":"از خودتون پذیرایی کنید","I mean it!":"جدی میگم",
"Why?to what end?":"چرا؟ به چه منظور؟","Bye for now!":"فعلا خداحافظ","You just say the world!":"فقط لب تر کن",
"Come on keep your chin up!":"بی خیال اخماتو باز کن",
"Lesson 2":"",
"You had me at hello!":"از همون نگاه اول دلمو بردی","Just shut up,you had me at hello!":"فقط خفه شو! از همون نگاه اول دلمو بردی",
"I adore you!":"خیلی عاشقتم","I'm in love with you!":"عاشقتم","I'm realy in love with you!":"واقعا عاشقتم",
"I do love you!":"خیلی دوستت دارم","I think I'm in love with you!":"فکر کنم عاشقت شدم",
"I'm realy in love with your son":"من واقعا عاشق پسرتونم","I would die for you!":"میمیرم برات",
"I will never abandon you!":"هرگز ترکت نخواهم کرد","I'm crazy about you!":"دیونتم",
"I can't stop thinking about you!":"نمیتونم بهت فکر نکنم","I'm crazy about you,Isn't that enough?":"دیونتم! این کافی نیست؟",
"Lesson 3":"",
"Have it your way!":"هرکاری میخوای بکن","Pull yourself togetter!":"خودتو جمع و جور کن",
"Sorry to interrupt!":"ببخشید که حرفت رو قطع کردم","Don't interrupt me!":"حرفم رو قطع نکن",
"Lesson 4":"",
"You know, I  would die for you!":"میدونی میمیرم برات","I would die for him!":"میمیرم براش",
"I love you,I would die for you!":"دوست دارم، میمیرم برات","I'm so crazy about you!":"خیلی دیونتم",
"She/He is crazy about you!":"دیونته",
"Lesson 5":"",
"Who saw that coming!":"کی فکرشو میکرد","I saw that coming!":"میدونستم اینطوری میشه",
"Nobody saw that/this coming!":"هیشکی فکرشو نمیکرد اینطوری بشه",
"I did not see that coming!":"اصلا فکرشم نمیکردم اینطوری بشه","Didn't see that coming!":"اصلا فکرشم نمیکردم اینطوری بشه",
"Lesson 6":""}

ListOfTheKeys=list(DicOfSentenses.keys())


case=input(""" Hi! \n If you want to review the whole of Lessons respectively; ENTER "w"
 \n If you want to review some of the Lessons; ENTER "l"
 \n If you want to review some of the sentences randomly; ENTER "r"
 \n If you want to insert the new sentences; ENTER "i" 
 \n If you want to exit the program; ENTER "e" """)

while (case!='w' and case!='l' and case!='r' and case!='i' and case!='e'):
    case=input(""" Hi! \n If you want to review the whole of Lessons respectively; ENTER "w"
 \n If you want to review some of the Lessons; ENTER "l"
 \n If you want to review some of the sentences randomly; ENTER "r"
 \n If you want to insert the new sentences; ENTER "i" 
 \n If you want to quit the program; ENTER "q" """)

if case=="w":
    for i in range(len(ListOfTheKeys)):
        print(ListOfTheKeys[i])
        StrKey=ListOfTheKeys[i]
        Answer=input("Please enter your answer:")
        if StrKey[:6]=="Lesson":
            print("\t \t The new lesson: \t %s " %(ListOfTheKeys[i]))
            continue
        elif Answer==DicOfSentenses[ListOfTheKeys[i]]:
            print("Your answer \t %s \t is correct" %(DicOfSentenses[ListOfTheKeys[i]]))
        else:
            print("Your answer \t %s \t is wrong" %(Answer))
            print("Answer is: \t %s" %(DicOfSentenses[ListOfTheKeys[i]]))
elif case=="l":
    Start=input("Please enter the Lesson that would you start(just enter a number):")
    End=input("Please enter the Lesson that would you end(just enter a number):")

    StrStart='Lesson '+Start
    StrEnd='Lesson '+str(int(End)+1)

    IndexStart=ListOfTheKeys.index(StrStart)
    IndexEnd=ListOfTheKeys.index(StrEnd)

    if IndexStart=="" or IndexEnd=="":
        print("There isn't this lossens!")
        IndexStart=ListOfTheKeys[0]
        IndexEnd=ListOfTheKeys[-1]


    for i in range(IndexStart,IndexEnd):
        print(ListOfTheKeys[i])
        StrKey=ListOfTheKeys[i]
        Answer=input("Please enter your answer:")
        if StrKey[:6]=="Lesson":
            print("\t \t The new lesson: \t %s " %(ListOfTheKeys[i]))
            continue
        elif Answer==DicOfSentenses[ListOfTheKeys[i]]:
            print("Your answer \t %s \t is correct" %(DicOfSentenses[ListOfTheKeys[i]]))
        else:
            print("Your answer \t %s \t is wrong" %(Answer))
            print("Answer is: \t %s" %(DicOfSentenses[ListOfTheKeys[i]]))

elif case=="r":

    Number=input("Please enter the number of sentences that you're going to review(just enter a number):")

    for i in range(int(Number)+1):
        RandomNumber=np.random.randint(len(ListOfTheKeys))
        print(ListOfTheKeys[RandomNumber])
        Answer=input("Please enter your answer:")
        if Answer==DicOfSentenses[ListOfTheKeys[RandomNumber]]:
            print("Your answer \t %s \t is correct" %(DicOfSentenses[ListOfTheKeys[RandomNumber]]))
        else:
            print("Your answer \t %s \t is wrong" %(Answer))
            print("Answer is: \t %s" %(DicOfSentenses[ListOfTheKeys[RandomNumber]]))

#elif case=="i":

elif case=="q":
    quit()
