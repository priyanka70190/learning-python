try:
  dict1={1:"samosa",2:"pakoda",3:"prontha"}
  print(dict1[4])
except Exception as e:
    print("KeyError occured: ",e)