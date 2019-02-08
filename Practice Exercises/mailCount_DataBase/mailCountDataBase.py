# Emails's domain name histogram in the form of a table inside a database. The
# file 'mbox.txt' was taken from http://data.pr4e.org/mbox.txt
import sqlite3,re
# Database creation
con = sqlite3.connect('mailCount.sqlite')
curs = con.cursor()

curs.execute('DROP TABLE IF EXISTS Counts')
curs.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')
# Required querys
org_qu = 'SELECT org FROM Counts WHERE org = ?'
newOrg_qu = 'INSERT INTO Counts (org,count) VALUES (?,1)'
updOrg_qu  = 'UPDATE Counts SET count = count + 1 WHERE org = ?'
results = 'SELECT org,count FROM Counts ORDER BY count DESC LIMIT 10'

hand = open('mbox.txt')
for ln in hand:
    ln = ln.rstrip()
    numIter = numIter + 1
    if re.search('^From: ',ln):
        # Extract the email domain name as strings
        org = re.findall('\S+@(\S+)',ln)[0]
    else:
        continue
    curs.execute(org_qu, (org,) )
    if curs.fetchone() is None:
        curs.execute(newOrg_qu, (org,) )
    else:
        curs.execute(updOrg_qu, (org,) )
    con.commit()
# Show info
for row in curs.execute(results):
    print(str(row[0]),row[1])

# Close connection
con.close()
