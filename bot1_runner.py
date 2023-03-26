from bot1_project import main

while True:
   try:
      main() # assuming this has a blocking loop as well
   except Exception as e:
      print(e) # or log it in some way
   print("Restarting main")
