import time
from plyer import notification

#every answer I get I want it to be stip and lower
def ans(msg):
    msg = msg.lower()
    msg = msg.strip()
    return msg

#do you wanna play
def welcomeMsg():
    flag = True
    while flag:
        answer = input ("Whould you like to play? (yes or no): ")
        if ans(answer) == "yes":
            flag =not flag
        elif ans(answer) == "no":
            print("Pussie")
            flag =not flag
        else :
            print("really now you are not funny... lets try again")
    return answer


#most of the time I want a sec delay when the I output a msg.
def say(msg):
    print (msg)
    time.sleep(1)

def notif(msg):
    notification.notify(title="Stories Unread", message=msg,app_name="cmd game",timeout=10)

#the begging of the story
def maingame():
    class Player:
        name = "Bob"
        hp = 100
    #Phase 1: the begginging
    say ("You woke up here...")
    say ("<<Who am I? >>... \nAs it seams you hit your head very hard you don't even remember your name")
    answer =input ("I have a name for you... or you can choose your own... (if you want a custome name type: no I have a name) ")
    if ans(answer) == "no i have a name":
        Player.name = input ("Well I am waiting: ")
        time.sleep(1)
        print ("really that's what you want to call youself\nWhatever hey " ,Player.name," this is you hp" ,Player.hp,"/100")
        time.sleep(3)
    else:
        print("well in that case I will call you...\n...")
        time.sleep(3)
        print ( Player.name )
        time.sleep(2)
        print("yes")
        time.sleep(2)
        print (Player.name)
        time.sleep(1)
        print ("Well Bob let me tell you this is you hp" , Player.hp)
        time.sleep(1)
    #Phase 2: can You servive?
    say ("\n\nLook arround you\n")
    print ("\nthere is Noooooothing only trees you have been lost in the forest ",Player.name)
    time.sleep(1)
    say ("\ndo not even try it there is no signal")
    flag = True 
    while flag:
        say ("\nYou can try to escape or you can look for resources (leave/resources)")
        answer =input()
        if ans(answer) == "leave":
            on_the_move(Player)
            flag =not flag
        elif ans(answer)=="resources":
            stay(Player)
            flag= not flag
        else: say ("sorry I didn't get that")

#first desion tree



#this is what happens if you leave
def on_the_move(Player):
    print ("Well let me tell you ", Player.name, " in every survival guide ever they say first if you are in the woods is\n\n")
    time.sleep(2)
    say ("LOOK FOR REASOURCES ")
    notif("REASOURCES")
    say ("\nBut I guess you know better") 


#this is what happens if you go out to look for resources
def stay(Player):
    say("looks like you are a smart one")


def main():
    print("---Welcome to the Stories Unread----")
    willYouPlay = welcomeMsg()
    if willYouPlay.lower().strip() == "yes":
        maingame()
if __name__ == "__main__":
    main()