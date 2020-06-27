xxx datetime;
currentdate = datetime.datetime.now()
s = 'D:\\Repeaters\\Repeaters_Log_'+ currentdate.strftime("%d-%m-%Y") + '.txt'
c = 'D:\\Repeaters\\Repeaters_Results_'+ currentdate.strftime("%d-%m-%Y") + '.txt'
sum = 0
sum_nok = 0
f = open(s)
if 'Snapshots of Vedrina taken' in f.read():
    t = open(c, 'w')
    t.write('Vedrina - OK\n')
    t.close()
    sum = sum + 1

else:
    t = open(c, 'w')
    t.write('Vedrina - NOK\n')
    t.close()
    sum_nok = sum_nok + 1

f.seek(0)
t = open(c, 'a')
if 'Snapshots of Fouren taken' in f.read():
    t.write('Fouren - OK\n')
    sum = sum + 1

else:
    t.write('Fouren - NOK\n')
    sum_nok = sum_nok + 1

f.seek(0)
if 'Snapshots of Dedraks taken' in f.read():
    t.write('Dedraks - OK\n')
    sum = sum + 1

else:
    t.write('Dedraks - NOK\n')
    sum_nok = sum_nok + 1

f.seek(0)
if 'Snapshots of Virovsko taken' in f.read():
    t.write('Virovsko - OK\n')
    sum = sum + 1

else:
    t.write('Virovsko - NOK\n')
    sum_nok = sum_nok + 1

f.seek(0)
if 'Snapshots of Hotnitsa taken' in f.read():
    t.write('Hotnitsa - OK\n')
    sum = sum + 1

else:
    t.write('Hotnitsa - NOK\n')
    sum_nok = sum_nok + 1

f.seek(0)
if 'Snapshots of Staropatitsa taken' in f.read():
    t.write('Staropatitsa - OK\n')
    sum = sum + 1

else:
    t.write('Staropatitsa - NOK\n')
    sum_nok = sum_nok + 1

f.seek(0)
if 'Snapshots of Yassen taken' in f.read():
    t.write('Yassen - OK\n')
    sum = sum + 1

else:
    t.write('Yassen - NOK\n')
    sum_nok = sum_nok + 1

f.seek(0)
if 'Snapshots of Vurbitsa_Vratsa taken' in f.read():
    t.write('Vurbitsa_Vratsa - OK\n')
    sum = sum + 1

else:
    t.write('Vurbitsa_Vratsa - NOK\n')
    sum_nok = sum_nok + 1

f.seek(0)
if 'Snapshots of Bukovets taken' in f.read():
    t.write('Bukovets - OK\n')
    sum = sum + 1

else:
    t.write('Bukovets - NOK\n')
    sum_nok = sum_nok + 1

f.seek(0)
if 'Snapshots of Gorovo taken' in f.read():
    t.write('Gorovo - OK\n')
    sum = sum + 1

else:
    t.write('Gorovo - NOK\n')
    sum_nok = sum_nok + 1

f.seek(0)
if 'Snapshots of Vurbitsa_Pleven taken' in f.read():
    t.write('Vurbitsa_Pleven - OK\n')
    sum = sum + 1

else:
    t.write('Vurbitsa_Pleven - NOK\n')
    sum_nok = sum_nok + 1

f.seek(0)
if 'Snapshots of Gougoutka taken' in f.read():
    t.write('Gougoutka - OK\n')
    sum = sum + 1

else:
    t.write('Gougoutka - NOK\n')
    sum_nok = sum_nok + 1

f.seek(0)
if 'Snapshots of Kozloduy_NPP taken' in f.read():
    t.write('Kozloduy_NPP - OK\n')
    sum = sum + 1

else:
    t.write('Kozloduy_NPP - NOK\n')
    sum_nok = sum_nok + 1

f.seek(0)
if 'Snapshots of Gorno_Negushevo taken' in f.read():
    t.write('Gorno_Negushevo - OK\n')
    sum = sum + 1

else:
    t.write('Gorno_Negushevo - NOK\n')
    sum_nok = sum_nok + 1

f.seek(0)
if 'Snapshots of Bultime taken' in f.read():
    t.write('Bultime - OK\n')
    sum = sum + 1

else:
    t.write('Bultime - NOK\n')
    sum_nok = sum_nok + 1

f.seek(0)
if 'Snapshots of Masterhaus_Ravda taken' in f.read():
    t.write('Masterhaus_Ravda - OK\n')
    sum = sum + 1

else:
    t.write('Masterhaus_Ravda - NOK\n')
    sum_nok = sum_nok + 1

f.seek(0)
if 'Snapshots of Masterhaus_Primorsko taken' in f.read():
    t.write('Masterhaus_Primorsko - OK\n')
    sum = sum + 1

else:
    t.write('Masterhaus_Primorsko - NOK\n')
    sum_nok = sum_nok + 1

f.seek(0)
if 'Snapshots of Milchev taken' in f.read():
    t.write('Milchev - OK\n')
    sum = sum + 1

else:
    t.write('Milchev - NOK\n')
    sum_nok = sum_nok + 1

f.seek(0)
if 'Snapshots of Amer_Sport taken' in f.read():
    t.write('Amer_Sport - OK\n')
    sum = sum + 1

else:
    t.write('Amer_Sport - NOK\n')
    sum_nok = sum_nok + 1

f.seek(0)
if 'Snapshots of Brushlen taken' in f.read():
    t.write('Brushlen - OK\n')
    sum = sum + 1

else:
    t.write('Brushlen - NOK\n')
    sum_nok = sum_nok + 1

f.seek(0)
if 'Snapshots of Raklinovo taken' in f.read():
    t.write('Raklinovo - OK\n')
    sum = sum + 1

else:
    t.write('Raklinovo - NOK\n')
    sum_nok = sum_nok + 1

f.seek(0)
if 'Snapshots of Euro07 taken' in f.read():
    t.write('Euro07 - OK\n')
    sum = sum + 1

else:
    t.write('Euro07 - NOK\n')
    sum_nok = sum_nok + 1

f.seek(0)
if 'Snapshots of Sport_Club_Management taken' in f.read():
    t.write('Sport_Club_Management - OK\n')
    sum = sum + 1

else:
    t.write('Sport_Club_Management - NOK\n')
    sum_nok = sum_nok + 1

f.seek(0)
if 'Snapshots of Atik_Plovdiv taken' in f.read():
    t.write('Atik_Plovdiv - OK\n')
    sum = sum + 1

else:
    t.write('Atik_Plovdiv - NOK\n')
    sum_nok = sum_nok + 1

f.seek(0)
if 'Snapshots of Agroelit_Buinovo taken' in f.read():
    t.write('Agroelit_Buinovo - OK\n')
    sum = sum + 1

else:
    t.write('Agroelit_Buinovo - NOK\n')
    sum_nok = sum_nok + 1

f.seek(0)
if 'Snapshots of Metal_Trade_Vitanovtsi taken' in f.read():
    t.write('Metal_Trade_Vitanovtsi - OK\n')
    sum = sum + 1

else:
    t.write('Metal_Trade_Vitanovtsi - NOK\n')
    sum_nok = sum_nok + 1

f.seek(0)
if 'Snapshots of Bulgartabak taken' in f.read():
    t.write('Bulgartabak - OK\n')
    sum = sum + 1

else:
    t.write('Bulgartabak - NOK\n')
    sum_nok = sum_nok + 1

f.seek(0)
if 'Snapshots of Iskur_Lake taken' in f.read():
    t.write('Iskur_Lake - OK\n')
    sum = sum + 1

else:
    t.write('Iskur_Lake - NOK\n')
    sum_nok = sum_nok + 1

f.seek(0)
if 'Snapshots of Samuil taken' in f.read():
    t.write('Samuil - OK\n')
    sum = sum + 1

else:
    t.write('Samuil - NOK\n')
    sum_nok = sum_nok + 1

f.seek(0)
if 'Snapshots of Kaufland_Dupnitsa taken' in f.read():
    t.write('Kaufland_Dupnitsa - OK\n')
    sum = sum + 1

else:
    t.write('Kaufland_Dupnitsa - NOK\n')
    sum_nok = sum_nok + 1

t.write('\n' + str(sum) + ' repeater(s) are OK. Snapshots are taken.')
t.write('\n' + str(sum_nok) + ' repeater(s) are NOK. Snapshots are NOT taken.')
t.close()
f.close()