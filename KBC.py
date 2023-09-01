questions = [
  [
    "Q1 Arrange these words from a slogan raised by Bal Gangadhar Tilak in the correct order", "Mera", "Swaraj", "Adhikar Hai",
    "Janmasiddha","badc"
  ],
  [
    "Q2 Name the capital of Russia", "Kazan", "Penza", "moscow",
    "Rostov-on-Don","c"
  ],
  [
    "Q3 Who was the First Batsman ever to score a century for India in Test Cricket?", "Lala Amarnath Bhardwaj", "Kapil Dev", "Rahul Dravid",
    "Farukh Engineer","a"
  ],
  [
    "Q4 How many times did India win the ICC Cricket World Cup?", "3", "2", "1",
    "4","b"
  ],
  [
    "Q5 Which is the largest state in India by area", "Uttar Pradesh", "Madhya Pradesh", "Maharastra",
    "Rajasthan","d"
  ],
  [
    "Q6 The age of retirement of High Court Judge", "65", "60", "62",
    "58","c"
  ],
  [
    "Q7 Minimum Age of the member of Rajyasabha", "25", "21", "35",
    "30","d"
  ],
  [
    "Q8 How many fundamental rights granted initially", "7", "6", "4",
    "5","a"
  ],
  [
    "Q9 What does the C stands for in the Einstein's Equation E = mc^2", "constant", "kinetic energy", "candela",
    "speed of light","d"
  ],
  [
    "Q10 The raindrops take up the spherical shape due to the .......... of water", "viscosity", "surface tension", "density",
    "pressure","b"
  ],
  [
    "Q11 Whose idea was it to start Jawahar Navodaya Vidyalayas?", "Jawahar Lal Nehru", "Atal Bihari Vajpayee", "Indira Gandhi",
    "Rajeev Gandhi","d"
  ]
]

levels = [100, 200, 300, 500, 1000, 2000, 4000, 8000, 16000, 32000, 64000]

money = 0
h = 0
a = 0
for i in range(0, len(questions)):
  
  question = questions[i]
  print(f"\n\nQuestion for Rs. {levels[i]}")
  print(f"{question[0]}")
  print(f"a. {question[1]}          b. {question[2]} ")
  print(f"c. {question[3]}          d. {question[4]} ")

  if h<2 :
    try :
        print("Do you want to take your helpline ?")
        Tellme = int(input("press any valid key for No or 1 for Yes : "))
        if Tellme == 1:
         if h == 0 :
            print("Choose your helpline")
            print("(a) Phone Call (b) Audience Poll")
            option = input("Enter your option a or b : ")
            if option == "a":
                print("Use your phone call")
                a = True
                h = h+1
            elif option == "b":
                print("Lets wait for audience poll")
                a = False
                h = h+1
         else : 
            if a == True:
                print("Lets wait for audience poll")
                h = h+1
            else :
                print("Use your phone call")  
                h = h+1
        else :
           print("OK")
    except ValueError : 
           print("")

                
  reply = input("Enter your option or  q to quit:\n" )
  if(reply == "q"):
    if i == 0 :
       money = 0
       break
    else :
       money = levels[i-1]
       break
  if(reply == question[-1]):
    print(f"Correct answer, you have won Rs. {levels[i]}")
    if(i == 3):
      money = 500
    elif(i == 5):
      money = 2000
    elif(i == 7):
      money = 8000
  else:
    print("Wrong answer!")
    print(f"Correct answer is option {question[-1]}")
    break 
  if i == 10 :
     print("!!!!! Congratulations !!!!!!")

print(f"Your take home money is {money}")