from playsound import playsound
print('''
.....# Welcome To you in KBC #..... 
''')

questions=[
    " 1.How many continents in the world?",
    " 2.Which day is observed as the world standard day?",
    " 3.what is the national food of Navgurukul?",
    " 4.Who is the author of the epic 'Magdoot'?",
    " 5.September 27 is celebrated every year as?",
    " 6.How many planets are there in our solar system?",
    " 7.Who is the president of America?",
    " 8.Where is the Navgurukul's girls campus in India?",
    " 9.Who's that person name who said that 'Me madharchood hu jo yaha aaya'",
    " 10.Who is Binod?",
    " 11.How many stairs steps are in our campus?"
    ]
options=[
    ["1","5","4","7","50:50"],
    ["June 26","Oct 14","Nov 15","Dec 2","50:50"],
    ["Rice","Fried","Fried Rice","Dal","50:50"],
    ["Vamlmiki","Banabhata","Kalidas","Vishal","50:50"],
    ["Teacher,s Day","Natinal Integretion Day","World Tourism Day","International Day","50:50"],
    ["5","8","9","6","50:50"],
    ["Joe Biden","Donald Trump","Emmanuel Macron","Barack Obama","50:50"],
    ["Pune","Banglore","Delhi","Gurugram","50:50"],
    ["Baloon Wala","Parachute Wala","Ship Wala","Circus Wala","50:50"],
    ["Riyaz","Peter","Abhi Pata nhi hai","Deepak","50:50"],
    ["16","15","13","14","50:50"]
    ]
solutions=[4,2,3,3,3,2,1,2,2,3,1]
sol=[
    [2,4],
    [2,3],
    [2,3],
    [3,1],
    [4,1],
    [2,4],
    [4,1],
    [2,4],
    [2,3],
    [2,1],
    [4,3]
] 
n1=0
n=0
# question's option counter
k=1
# for option number printing
d=0
# for 50:50 counter
for i in questions:      
    print(i)
    if n1==0:
            playsound("How many continents in the world.mp3")
    elif n1==1:
        playsound("Which day is observed as the world standard day.mp3")
        
    elif n1==2:
        playsound("what is the national food of Navgurukul.mp3")
            
    elif n1==3:
        playsound('''Who is the author of the epic "Magdoot".mp3''')
            
    elif n1==4:
        playsound("September 27 is celebrated every year as.mp3")
            
    elif n1==5:
        playsound("How many planets are there in our solar system.mp3")
        
    elif n1==6:
        playsound("a.mp3")
        
    elif n1==7:
        playsound("g.mp3")
        
    elif n1==8:
        playsound("m.mp3")
        
    elif n1==9:
        playsound("Who is Binod.mp3")
    elif n1==10:
        playsound("h.mp3")
 
    print('''     Here Is Your Options...
    ''')
    for i in options[n]:
        if k==6:
            k=1
        print(" "+str(k),':', i)
        k+=1
    inp=int(input('''
 Choose Your Answer:'''))
    playsound("c.mp3")
    if inp==solutions[n]:
        print('''
 Congratulation! You Won
        ''')
        playsound("congrats.mp3")
    elif inp==5:
        if d==1:
            print('''
 Sorry!! You Already Choosed This 50:50 option
            ''')
            playsound("Sorry!! You Already Choosed This 50:50 option.mp3")
        else:
            for i in range(1):
                print(''' Choose Your 50:50 Answer:''', sol[n])
                playsound("5050.mp3")
            inp=int(input(''' Choose Your Answer:'''))
            playsound("c.mp3")
            if inp==solutions[n]:
                print(''' Congratulation! You Won Again
                ''')
                playsound("congrates.mp3")
                d+=1
    else:
        print('''Your Answer Is Wrong.''')
        playsound("wrong.mp3")
        break
    n+=1
    n1+=1