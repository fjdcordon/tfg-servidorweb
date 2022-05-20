from django.shortcuts import render
from .funciones import *

def main(request):
   if not validarCookie(request.COOKIES.get('id')):
        return redirect("/login")
   else:
      return redirect("/monitor")

def login(request, template_name="login.html"):
    if validarCookie(request.COOKIES.get('id')):
        return redirect("/monitor")
    else:
        return render(request, template_name)

def monitor(request, template_name="monitor.html"):

    cookie = request.COOKIES.get('id')

    if validarCookie(cookie):

        try:
            status = send2gw(2)
            inclinacion = send2gw(1)
            energia = send2gw(0)

            if status[0] == 1 or inclinacion[0] == 1 or energia[0] == 1:
                return HttpResponse("Se ha producido un error en la carga de datos. Contacte con el administrador.")
            else:
                args = {'user': getUser(cookie), 'status': send2gw(2)[1], 'inclinacion': send2gw(1)[1], 'energia': send2gw(0)[1]}
                return render(request, template_name, args)
        except:
            return HttpResponse("Se ha producido un error en la carga de datos. Contacte con el administrador.")
    else:
        return redirect('/login')

def authUser(request):
    if not validarCookie(request.COOKIES.get('id')) and request.method == 'POST':
        return autenticacion(request.POST['user'], request.POST['pass'])
    else:
        return redirect("/login")

def logout(request):
    cookie = request.COOKIES.get('id')
    if validarCookie(cookie):
        if not eliminarCookie(cookie):
            return HttpResponse("Error al cerrar sesión. Contacte con el administrador.")

    return redirect("/login")

def cambiarEstado(request):
    cookie = request.COOKIES.get('id')
    if validarCookie(cookie):
        if request.POST['submit_estado'] == "Encender":
            send2gw(3)
        else:
            send2gw(4)

        return redirect("/monitor")
    else:
        return redirect("/login")

def moverPlaca(request):
    cookie = request.COOKIES.get('id')
    if validarCookie(cookie):
        send2gw(5, content=request.POST['angulo'])
        return redirect("/monitor")
    else:
        return redirect("/login")

