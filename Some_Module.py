class Hello:
  def __init__(self, name):
    self.name = name
  
  def say(self):
    print("Hello " + self.name)

  def ask_name(self):
    self.name = input("Input name: ")
    
