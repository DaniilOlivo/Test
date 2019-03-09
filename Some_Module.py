class Hello:
  def __init__(self, name):
    self.name = name
  
  def say(self):
    print("Hello {}!".format(self.name))

  def ask_name(self):
    self.name = input("Input name: ")

  def many_hello(self, count):
    for i in range(count):
      self.say()

  def abyyyyyyy(self):
    print('Abyyyyyyyyyyyyyy!')
    
