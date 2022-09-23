import datetime
x = input("Enter For time Start: ")
start = datetime.datetime.now()

y = input("Enter For time Stop: ")
end = datetime.datetime.now()

res = end - start
print("Time Diffrance between start and stop time: ", res)
