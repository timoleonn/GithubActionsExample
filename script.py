from datetime import datetime

# datetime object containing current date and time
now = datetime.now()
dt_string = now.strftime("%d-%m-%Y_%H-%M-%S")

filename = "myfile_{}.txt".format(dt_string)

f = open(filename, "x")
f.close()
