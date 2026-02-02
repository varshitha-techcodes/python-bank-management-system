import mysql.connector as db
con=db.connect(user='root',password='sql@123',host='localhost',database='Bank')
cur=con.cursor()

def db_query(str_query):
    cur.execute(str_query)
    result = cur.fetchall()
    return result

def createcustomertable():
    cur.execute("""create table if not exists customer(
            username varchar(30) not null,
            password varchar(20) not null,
            name varchar(20)not null,
            age int not null,
            city varchar(20)not null,
            account_number bigint not null,
            balance bigint not null,
            status boolean not null);
    """)
con.commit()
    
if __name__=="__main__":
    createcustomertable()
cur.close()
con.close()



