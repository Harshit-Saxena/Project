command = ""
started = False
print("Type help to see the commands")
while True:
     command = input(">: ").lower()
     if command == "start":
          if started: # This means if started = True
               print("Car is already moving !!")
          else:
               started = True
               print("Car has started")
     elif command == "stop":
          if not started: # This means is started = False (If not started = True) and not converts bool value to opp
               print("Car has already stopped !!")
          else: 
               started = False
               print("Car has stopped")
     elif command == "help":
          print("""
start: To make the car move
stop: To make the car stop
quit: To exit the program
          """)
     elif command == "quit":
          break
     else:
          print("Sorry I didn't understand that")