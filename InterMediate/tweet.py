'''Tweet a Random Followers'''

#To install twitter for python , Run command in in command
#  users>>pip install python-twitter

#Get the followers
import twitter
import random 

print ("Hello Tweeter")

#BElow Code is for connecting tweeter developers account info
api = twitter.Api(consumer_key='slLD7aG6zS2LnMyxM0HGS5RDy',
                      consumer_secret='VIpGqlkEsqTMS4X1zlutN47aGksKWadJhHBR0MnW8tXjuWHTEv',
                      access_token_key='1351407135599415298-3aMCBxsB4hNdfq9qxFxJzQpaGSFrSu',
                      access_token_secret='EmAsa2FD80BFgU0wE6MdG9ohqENydzhHIdjZsL0wwunBu')
#print(api.VerifyCredentials())
users=api.GetFriends()

print([u.name for u in users])
print(len(users))

followers=api.GetFollowers()
print(len(followers))
print([u.name for u in followers])

randomIndex=random.randint(0,len(followers)-1)
randomFollower=followers[randomIndex]

print(randomFollower.screen_name)

tweet="@{} you are random follower of the Day (through a Python Programming.) How r u Buddy?".format(randomFollower.screen_name)

print(tweet)

api.PostUpdate(tweet)
#IMP : you can call api for 15 times in 15 mins as tweeter window is open for 15 mins

print("Thanks for tweeting")