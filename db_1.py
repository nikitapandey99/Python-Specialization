import sqlite3

connection=sqlite3.connect('emaildb.sqlite')
curs=connection.cursor()

curs.execute('DROP TABLE IF EXISTS Counts')
curs.execute('CREATE TABLE Counts (email TEXT, count INTEGER)')

fname=input('Enter a file:')
if len(fname)<1 :fname='mbox-short.txt'
fh=open(fname)
for line in fh:
    if not line.startswith('From: '):continue
    lst=line.split()
    email=lst[1]
    curs.execute('SELECT count FROM Counts WHERE email=?',(email,))
    row=curs.fetchone()
    if row is None:
        curs.execute('INSERT INTO Counts (email,count) VALUES (?,1)',(email,))
    else:
        curs.execute('UPDATE Counts SET count=count+1 WHERE email=?',(email,))
    #print('next')
connection.commit()

sqlstr='SELECT email,count FROM Counts ORDER BY count DESC LIMIT 10'

for row in curs.execute(sqlstr):
    print(str(row[0]),row[1])
curs.close()
