import datetime
import hashlib
import uuid
import mysql.connector
from django.http import HttpResponse
from django.shortcuts import redirect
from mysql.connector import Error
import socket
from .protocols import propProto

def abrirConex():
    mydb = mysql.connector.connect(
        host="localhost",
        user="servWeb",
        password="servWeb",
        database="servWeb"
    )

    return mydb

def validarCookie(cookie):
    try:
        conn = abrirConex()
        mycursor = conn.cursor()
        sql = """SELECT exp_tstamp from cookies WHERE ID=%s"""
        mycursor.execute(sql, [cookie])
        r = mycursor.fetchone()
        mycursor.close()
        conn.close()
        if r == None:
            return False
        else:
            if datetime.datetime.now().timestamp() < float(r[0]):
                return True
            else:
                return False
    except:
        return False

def getUser(cookie):
    try:
        conn = abrirConex()
        mycursor = conn.cursor()
        sql = """SELECT user FROM cookies WHERE ID=%s"""
        mycursor.execute(sql, [cookie])
        r = mycursor.fetchone()
        mycursor.close()
        conn.close()
        return r[0]
    except:
        return None

def eliminarCookie(cookie):
    try:
        conn = abrirConex()
        mycursor = conn.cursor()
        sql = """DELETE FROM cookies WHERE ID=%s"""
        mycursor.execute(sql, [cookie])
        conn.commit()
        mycursor.close()
        conn.close()
        return True
    except:
        return False

def autenticacion(user, password):

    try:
        conn = abrirConex()
        mycursor = conn.cursor()
        sql = "SELECT 1 FROM users WHERE user='%s' AND pass='%s'" % (user, hashlib.sha256(password.encode('utf-8')).hexdigest())
        mycursor.execute(sql)
        r = mycursor.fetchone()
        if r is None:
            return HttpResponse("<script>alert('Usuario o contraseña incorrectos');window.location.replace('/login')</script>")

        max_age = 15 * 24 * 60 * 60
        exp_tstamp = (datetime.datetime.today() + datetime.timedelta(days=15)).timestamp()

        while r is not None:
            ident = str(uuid.uuid4())
            sql = """SELECT 1 from cookies WHERE ID=%s"""
            mycursor.execute(sql, [ident])
            r = mycursor.fetchone()

        sql = """INSERT INTO cookies(ID, user, exp_tstamp) VALUES(%s,%s,%s)"""
        mycursor.execute(sql, [ident, user, exp_tstamp])
        conn.commit()
        mycursor.close()
        conn.close()
        redir = redirect("/monitor")
        redir.set_cookie('id', ident, max_age=max_age)
        return redir

    except Error:
        return HttpResponse("Se ha producido un error. Contacte con el administrador.")


def send2gw(action, content=None):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('10.0.0.10', 5555)
    sock.connect(server_address)

    try:
        packet = propProto(action=action, error=0, content=content)
        sock.sendall(bytes(packet))
        data = sock.recv(50)
        sock.close()

        if data:
            recv_packet = propProto(data)
            pkt_type = getattr(recv_packet, "type")
            pkt_action = getattr(recv_packet, "action")
            pkt_error = getattr(recv_packet, "error")
            pkt_content = getattr(recv_packet, "content").decode('utf-8')

            if pkt_type == 1 and 5 >= pkt_action >= 0 == pkt_error:
                return 0, pkt_content
            else:
                return 1, None
        else:
            return 1, None
    except:
        return 1, None