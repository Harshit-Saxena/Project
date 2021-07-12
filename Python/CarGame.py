from playsound import playsound
playsound('C:\VScode\JavaScript\Python\Sound\Horn.mp3')
command = ""
started = False
print("Type help to see the commands")
while True:
     command = input(">: ").lower()
     if command == "start":
          if started: # This means if started = True
               print("Car is already moving !!")
               playsound('C:\VScode\JavaScript\Python\Sound\moving.wav')
          else:
               started = True
               print("Car has started")
               playsound('C:\VScode\JavaScript\Python\Sound\start.wav')

     elif command == "stop":
          if not started: # This means is started = False (If not started = True) and not converts bool value to opp
               print("Car has already stopped !!")
               playsound('C:\VScode\JavaScript\Python\Sound\stopped.wav')
          else: 
               started = False
               print("Car has stopped")
               playsound('C:\VScode\JavaScript\Python\Sound\stop.mp3')
               
     elif command == "help":
          playsound('C:\VScode\JavaScript\Python\Sound\help.mp3')
          print("""
start: To make the car move
stop: To make the car stop
quit: To exit the program
          """)
     elif command == "quit":
          playsound('C:\VScode\JavaScript\Python\Sound\quit.wav')
          break
     else:
          print("Sorry I didn't understand that")