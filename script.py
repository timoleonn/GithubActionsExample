from datetime import datetime

# datetime object containing current date and time
now = datetime.now()

filename = "myfile_{}".format(now)
f = open(filename, "x")
f.close()
