class player:
  def player(self):
      print("The player is playing cricket.")
class Batsman(player):
  def play (self):
      print("The Batsman is batting.")
class Bowler(player):
  def play(self):
      print("The bowler is bowling.")
batsman = Batsman()
bowler = Bowler()
batsman.play()
bowler.play()