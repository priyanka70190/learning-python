try:
    list=[1,2,3,4]
    print(list[4])
except IndexError as e:
    print("IndexError Occured:",e)