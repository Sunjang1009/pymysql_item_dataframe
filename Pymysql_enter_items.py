import sys
import os
import pymysql

config = {
    'host' : '127.0.0.1',
    'user' : 'root',
    'password' : 'root1234',
    'database' : 'mydb02',
    'charset' : 'utf8',
    'use_unicode' : True
}

try: 
    conn = pymysql.connect(**config)
    cursor = conn.cursor()
    sql = """create table if not exists tb6(
        code int primary key,
        name varchar (30) not null,
        su int default 0,
        dan int default 0
    )"""
    cursor.execute(sql)
    conn.commit()
except Exception as e:
    print('db connection error',e)
    conn.rollback()
finally:
    cursor.close()
    conn.close()
    
if __name__ == '__main__':
    while True:
        print('\t[menu for record]')
        print('1:search')
        print('2:adding items')
        print('3:edit')
        print('4:delete')
        print('5:program end')
        
        sel = int(input('enter item number: '))
        
        if sel == 1:
            try:
                conn = pymysql.connect(**config)
                cursor = conn.cursor()
                sql = "select * from tb6"
                cursor.execute(sql)
                rows = cursor.fetchall()
                for row in rows:
                    print(row)
            except Exception as e:
                print('db connection error',e)
                conn.rollback()
            finally:
                cursor.close()
                conn.close()
            os.system('pause')
        if sel == 2:
            try:
                conn = pymysql.connect(**config)
                cursor = conn.cursor()
                in_code = int(input('enter item code: '))
                in_name = input('enter item: ')
                in_su = int(input('enter quantity: '))
                in_dan = int(input('enter price: '))
                sql = f"insert into tb6 values({in_code},'{in_name}',{in_su},{in_dan})"
                cursor.execute(sql)
                conn.commit()
                
            except Exception as e:
                print('db connection error',e)
                conn.rollback()
            finally:
                cursor.close()
                conn.close()
            os.system('pause')

        if sel == 3:
            try:
                conn = pymysql.connect(**config)
                cursor = conn.cursor()
                in_code = int(input('enter item code to be edited: '))
                in_su = int(input('enter item quantity to be edited: '))
                in_dan = int(input('enter item price to be edited: '))
                sql = f"update tb6 set su = {in_su}, dan = {in_dan} where code = {in_code}"
                cursor.execute(sql)
                conn.commit()
                
            except Exception as e:
                print('db connection error',e)
                conn.rollback()
            finally:
                cursor.close()
                conn.close()
            os.system('pause')

        if sel == 4:
            try:
                conn = pymysql.connect(**config)
                cursor = conn.cursor()
                in_code = int(input('enter item to be deleted: '))
                sql = f"delete from tb6 where code = {in_code}"
                cursor.execute(sql)
                conn.commit()
                
            except Exception as e:
                print('db connection error',e)
                conn.rollback()
            finally:
                cursor.close()
                conn.close()
            os.system('pause')

        if sel == 5:
            print('program end')
            break
        else : 
            print('no item can be found')
            