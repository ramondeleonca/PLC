import colorama
import pyfiglet

print(
  colorama.Back.BLACK + 
  colorama.Fore.WHITE +
  pyfiglet.Figlet(font="avatar").renderText(
    "Hello! Welcome to my replit \n\n" +
    "Look around in the folders, there you'll find the activities :)"
  )
)