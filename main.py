from lib.f5cjsonp1 import f5cjsonp1

fileConf = open("tmp\input.conf", "r")
app1 = f5cjsonp1(fileConf.read())
app1.genTMSH()