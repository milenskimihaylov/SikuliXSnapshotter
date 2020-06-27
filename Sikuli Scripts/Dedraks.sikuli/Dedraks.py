xxx datetime;
currentdate = datetime.datetime.now()
s = 'D:\\Repeaters\\Repeaters_Log_'+ currentdate.strftime("%d-%m-%Y") + '.txt'
c = 'Dedraks'
f = open(s, 'a')
f.write('\n' + c +' script starts execution ' + currentdate.strftime("%H:%M") + '\n')
f.close()
click(Pattern("1542879657507.png").similar(0.90))

click(Pattern("1542880169863.png").similar(0.90))

dragDrop(Pattern("1541683903890.png").similar(0.80).targetOffset(-75,2), Pattern("1541683946919.png").similar(0.90).targetOffset(19,6))
type('(+359) xxx')
for x in range(3):
    click(Pattern("1541693652417.png").similar(0.80))
    hover(Pattern("1541684049033.png").similar(0.90))
    time.sleep(50)
    if exists(Pattern("1541691511061.png").similar(0.85),1) != None:
        break
find("1541684202039.png")
currentdate = datetime.datetime.now()
f = open(s, 'a')
f.write('Connected to ' + c + ' ' + currentdate.strftime("%H:%M") + '\n')
f.close()
type("1541684202039.png", 'xxx')

for i in range(3):
    click(Pattern("1541684400971.png").similar(0.85))
    hover("1541684461365.png")
    time.sleep(50)
    if exists(Pattern("1542893266942.png").similar(0.80),1) != None:
        break
find(Pattern("1542893266942.png").similar(0.80))
currentdate = datetime.datetime.now()
f = open(s, 'a')
f.write('Password for ' + c + ' accepted ' + currentdate.strftime("%H:%M") + '\n')
f.close()
click(Pattern("1542893266942.png").similar(0.80))
time.sleep(3)

waitVanish(Pattern("1543309633236.png").exact(),120)
currentdate = datetime.datetime.now()
f = open(s, 'a')
f.write('Stats for ' + c + ' loaded ' + currentdate.strftime("%H:%M") + '\n')
f.close()
click(Pattern("1542880917024.png").similar(0.90))
time.sleep(3)
click(Pattern("1542881195104.png").similar(0.80))
time.sleep(3)

dragDrop(Pattern("1542885643107.png").similar(0.95).targetOffset(-69,-40), Pattern("1542885675546.png").similar(0.80).targetOffset(71,30))


click(Pattern("1542881501167.png").similar(0.80))


dragDrop(Pattern("1542881644339.png").similar(0.90).targetOffset(163,-15), Pattern("1542881703313.png").similar(0.80).targetOffset(40,-8))

currentdate = datetime.datetime.now()
a = 'D:\\Repeaters\\Snapshots\\' + c +'_' + currentdate.strftime("%d-%m-%Y_%H-%M")
type(a)

click(Pattern("1542881798137.png").similar(0.90))


click(Pattern("1542884802777.png").similar(0.80).targetOffset(213,-30))
time.sleep(2)
if exists(Pattern("1543332827430.png").exact()) == None:
    
    click("1541685414532-1.png")

    click(Pattern("1542880917024-1.png").similar(0.90))
    time.sleep(3)
    click(Pattern("1542881195104-1.png").similar(0.80))
    time.sleep(3)
    dragDrop(Pattern("1542884991114-1.png").similar(0.90).targetOffset(-59,-28), Pattern("1542885022234-1.png").similar(0.90).targetOffset(65,43))

    click(Pattern("1542881501167-1.png").similar(0.80))
    dragDrop(Pattern("1542881644339-1.png").similar(0.90).targetOffset(163,-15), Pattern("1542881703313-1.png").similar(0.80).targetOffset(40,-8))
    currentdate = datetime.datetime.now()
    b = 'D:\\Repeaters\\Snapshots\\' + c +'_Alarms_' + currentdate.strftime("%d-%m-%Y_%H-%M")
    type(b)
    click(Pattern("1542881798137-1.png").similar(0.90))
    click(Pattern("1542884802777-1.png").similar(0.80).targetOffset(213,-30))
    time.sleep(2)
currentdate = datetime.datetime.now()
f = open(s, 'a')
f.write('Snapshots of ' + c + ' taken ' + currentdate.strftime("%H:%M") + '\n')
f.close()

click(Pattern("1542979556677.png").similar(0.80))
time.sleep(2)

click(Pattern("1541686059736.png").similar(0.80))
time.sleep(10)
click(Pattern("1541686088012.png").similar(0.80))
currentdate = datetime.datetime.now()
f = open(s, 'a')
f.write(c + ' operation is successful ' + currentdate.strftime("%d-%m-%Y_%H:%M") + '\n')
f.close()
