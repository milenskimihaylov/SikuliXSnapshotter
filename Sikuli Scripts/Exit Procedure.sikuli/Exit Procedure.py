xxx datetime;
currentdate = datetime.datetime.now()
s = 'D:\\Repeaters\\Repeaters_Log_'+ currentdate.strftime("%d-%m-%Y") + '.txt'
f = open(s, 'a')
f.write('______________________________________________________________________\n')
f.write('Exit procedure is starting ' + currentdate.strftime("%H:%M") + '\n')
f.close()
rightClick(Pattern("1542899025244.png").similar(0.80))
time.sleep(2)
click("1542899369063.png")
f = open(s, 'a')
f.write('Exit procedure is successful ' + currentdate.strftime("%H:%M") + '\n')
f.write('______________________________________________________________________\n')
f.write('----------------------------------------------------------------------\n')
f.close()


