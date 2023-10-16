#Define the player class
class Player:
def play(self):
print("The player is playing ceicket")
#Define the Batsman class
class Batman(Player):
def play(self):
print("The batsman is batting"):
#Define the Bowler class,derived from Player
class Bowler(Player):
def play(self):
print("The bowler is bowling"):
#Create objects of  batsman and bowler classes
batsman=Batsman()
bowler=Bowler()
#call the play method for each object
batsman.play()
bowler.play()