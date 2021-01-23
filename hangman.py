class Word():
  def __init__(self, chosen_word):
    self.chosen_word = chosen_word
    self.letters = list(chosen_word)
    self.record = {}
    self.letters_used = []
    self.remaining_guesses = 8

    # this method will split the word up into a list of dictionaries with 2 attributes:
    # the letter/character, and a boolean representing whether or not it has been guessed

  def to_dict(self):
    for i in self.letters:
      self.record[i] = False
  
  def check(self, let):
    if let in self.record:
      self.record[let] = True

  def game_turn(self):
    show_arr = []
    show_str = " "
    for i in self.letters:
        if (self.record[i] == True):
          show_arr.append(i)
        else:
          show_arr.append('_')
    print(show_str.join(show_arr))
    if '_' in show_arr:
      print(f'{self.remaining_guesses} guess remaining, guess a letter')
      guess = input()
      self.letters_used.append(guess)
      self.check(guess)
      self.remaining_guesses -= 1
    else:
      print('You win!')
      self.remaining_guesses = -1

  def game(self):
    self.to_dict()
    while(self.remaining_guesses > 0):
      self.game_turn()
    if self.remaining_guesses == 0:
      print('You lose')
      
    
apple = Word('apple')
apple.game()