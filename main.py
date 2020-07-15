from lib.f5cjsonp1 import f5cjsonp1

fileConf = open("tmp\input.conf", "r")
app1 = f5cjsonp1(fileConf.read())
fileConf.close()

listchangeStyle = app1.genTMSH()

fileConf = open("tmp\output.txt", "w")
alltxt = str()
for v1 in listchangeStyle:
    fileConf.write(v1 + "\n")
    print(v1)
fileConf.close()