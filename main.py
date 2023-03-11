print('Welcome to my computer quiz game')
play = input('DO you want to play? ')
score = 0
if play.lower() != "yes":
    quit()

answer = input("What does CPU stamds for? ")
if answer.lower() == "central processing unit" :
    print('correct!')
    score +=1
else:print('incorrect!')
answer = input("What does API stamds for? ")
if answer.lower() == "application programming interface" :
    print('correct!')
    score +=1
else:print('incorrect!')          
answer = input("What does https stamds for? ")
if answer.lower() == "hyper text transfer protocol" :
    print('correct!')
    score +=1
else:print('incorrect!')
answer = input("What does www stamds for? ")
if answer.lower() == "world wide web" :
    print('correct!')
    score +=1
else:print('incorrect!')

#print('you scored total' + ' '  + str(score)) 
print(f'you scored total {(score/4 * 100)}  %')



