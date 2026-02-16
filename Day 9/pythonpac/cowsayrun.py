# cowsay commands
import cowsay


def main():
  cowsayRunner()
  advancedCowsay()
  
  
def cowsayRunner():
  cowsay.cow("Hello, World!")
  cowsay.tux("Python is fun!")
  cowsay.dragon("Code like a dragon!")
  cowsay.ghostbusters("Who you gonna call?")
  cowsay.cheese("Say cheese!")
  cowsay.kitty("Meow meow!")
  cowsay.stegosaurus("Roar! I'm a stegosaurus!")
  cowsay.daemon("Beware the daemon!")
  cowsay.cow("Moo moo!")
  
  
 
def advancedCowsay():
   # Advanced cowsay usage
   message = "Advanced cowsay!"
   try:
     cowsay.dragon(message)
   except Exception:
     cowsay.cow(message)
    
  
if __name__ == "__main__":
  main()
