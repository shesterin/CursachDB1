

con = sqlite3.connect('dataset.db')
cur = con.cursor()
# cur.execute("""CREATE TABLE tablename(
#     phone INTEGER NOT NULL,
#     uid INTEGER NOT NULL,
#     mail TEXT,
#     first_name TEXT,
#     last_name TEXT,
#     gender TEXT,
#     date_registered TEXT,
#     birthday TEXT,
# );""")


with open('../Results/20241225_114747/dataset.csv', 'r', encoding="utf8") as f:
    dr = csv.DictReader(f, delimiter=",")
    to_db = [(i['phone'], i['uid'], i['email'], i['first_name'], i['last_name'], i['gender'], i['date_registered'], i['birthday']) for i in dr]

cur.executemany("INSERT INTO BD (phone, uid, email, first_name, last_name, gender, date_registered, birthday) VALUES (?, ?, ?);", to_db)
con.commit()
con.close()