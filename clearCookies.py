import time

import mysql
from apscheduler.schedulers.background import BackgroundScheduler

sched = BackgroundScheduler()

def limpiarCookies():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="servWeb",
            password="servWeb",
            database="servWeb"
        )
        mycursor = mydb.cursor()
        sql = """DELETE FROM cookies WHERE exp_tstamp<UNIX_TIMESTAMP(NOW());"""
        mycursor.execute(sql)
        mydb.commit()
        mycursor.close()
        mydb.close()

    except:
        print("Error")

def main():
    sched.add_job(limpiarCookies, trigger='cron', minute='0', hour='0', day='1')
    sched.start()

    try:
        while True:
            time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        sched.shutdown()


if __name__ == '__main__':
    main()