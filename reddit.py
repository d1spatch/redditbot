import praw, time, datetime, random

database = ["are you still doing this?", "seriously?", "really?", "uhuh", "uuuuh.... right", "don't you have anything better to do?", "Okay.", "seriously, you need a life.",  "please, you're being ridiculous. if you can't actually bring yourself to make intelligible comments maybe you shouldn't make any at all.", "So basically at this point you have absolutely no argument and are attempting a pyrrhic victory by wasting my time.", "you know for someone who's trying to put up a facade of indifference you sure reply a lot.", "This is actually quite fascinating, please go on. I can't wait to hear what else you'll say.", "Pathetic.", "I can't read what you wrote because I set RES to ignore you but I'm assuming you're apologizing for being stupid and telling me you've seen the error of your ways.", "and I'm saying you're wrong. bye now.", "bye now. for real.", "wrong again. take care now.", "Case in point...", "Oh no, a troll think's I'm wrong. My worldview is shattered.", "lol, that's a terrible comeback. Try again."]

user_agent = ("PRAW Troll Bot by /u/bad_code_no_treat v 0.1")
r = praw.Reddit(user_agent=user_agent)
r.login('login', 'hunter2')

submission = r.get_submission("")
target = ""

i = 0
replies = 0
time_start = datetime.datetime.now().replace(microsecond=0)
time_last_msg = time_start

print("* Script starting...")

responses = database

while True:
    try:
        print("* Checking for msgs...")
        for msg in r.get_unread(limit=None):
            #msg.submission == submission and 
            if( isinstance(msg, praw.objects.Comment ) and str(msg.author) == target ):
                if( len(reponses) <= 0 ):
                    reply = "Congratulations. You have been talking to a bot. Take this time to bask in your achievement, you beat a machine and it only took mere mintues of your life why I was elsewhere completely forgetting you exist. You may feel free to continue talking to the bot, but it will only generate responses previously given. Thank you and have a nice day."
                    responses = database
                else:
                    reply = random.choice(responses)
                    responses.remove(reply)
                print("     msg recieved from " + target + ": " + str(msg))
                msg.reply(reply)
                msg.mark_as_read()
                i += 1
                replies += 1
                time_last_msg = datetime.datetime.now().replace(microsecond=0)
                last_msg = msg
            elif( isinstance(msg, praw.objects.Comment) ):
                # if it's someone else, do some sort of check
                #   if someone else is arguing tell them  you're ignoring them.
                #   if someone says "i love you troll_bot, tell them you love them back
                #If PM is from target
                i = i
            elif( isinstance(msg, praw.objects.Message) and str(msg.author) == target ):
                #If PM is from someone else
                i = i
            elif( isinstance(msg, praw.objects.Message) ):
                # TODO: code that takes command input
                #       or handles messages    
                i = i
        time_now = datetime.datetime.now().replace(microsecond=0)
        time_up = time_now - time_start
        print("     Script run time: " + str(time_up))
        print("     Message last recieved from " + target + ": " + str(time_last_msg))
        print("     You have recieved " + str(replies) + " replies.")
        print("* Sleeping...")
        print("")
        time.sleep(120)
    except (RuntimeError, TypeError, NameError):
        raise
    
#praw.objects.Editable, praw.objects.Inboxable, praw.objects.Moderatable, praw.objects.Reportable, praw.objects.Voteable



