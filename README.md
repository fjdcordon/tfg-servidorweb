Servidor web de monitorización y control de una instalación fotovoltaica
=============

Este servidor web es uno de los componentes del escenario que se ha puesto en marcha para la realización de una prueba de concepto (PoC) que tiene como objetivo analizar las posibilidades de explotación de vulnerabilidades en entornos del Internet Industrial de las Cosas (IIoT). Este escenario está compuesto además por otros dos elementos: un componente OT, una simulación de un PLC industrial real ([PLC-SIM](https://github.com/fjdcordon/tfg-plc)); y un componente IoT, un [Gateway IoT](https://github.com/fjdcordon/tfg-gateway) que hace de interfaz IT/OT.

Para más información sobre el desarrollo de este escenario y la verificación de esta prueba de concepto se puede consultar mi Trabajo de Fin de Grado: «Análisis y explotación de vulnerabilidades en un sistema de monitorización y control remoto de energía solar».

Autor: Francisco Javier Domínguez Cordón

Instalación
-------------

1. Descargar la imagen ISO de Ubuntu Server 18.04.5: [Descargar Imagen](https://old-releases.ubuntu.com/releases/18.04.5/ubuntu-18.04-live-server-amd64.iso)

2. Dado que la infraestructura está virtualizada, hay que descargar un software de virtualización. En este caso, se ha optado por utilizar [Oracle VM VirtualBox](https://www.virtualbox.org/), un software de código abierto, gratuito y multiplataforma (Windows, GNU/Linux, Mac OS). Para instalarlo simplemente hay que seguir los pasos que se detallan en su página web.

3. Una vez instalado, lo abrimos y pulsamos sobre el botón *New* o *Nueva* (dependiendo del idioma en que este configurado el equipo anfitrión). Pondremos el nombre que deseemos a la máquina, indicaremos que se trata de un Linux y que la distribución es Ubuntu (64-bit). Dejaremos el resto de la configuración por defecto.

4. Una vez hecha la primera configuración de la máquina, vamos cambiar los ajustes de red. Para ello, hacemos click sobre la máquina y presionamos *Settings* o *Configuración*. Nos vamos a la opción de *Network* o *Red* y configuraremos el primer adaptador como *Bridged Adapter* o *Adaptador Puente* y el segundo adaptador como *Internal Network* o *Red Interna*. El nombre de la red interna será *intnet*.

5. Ahora iniciamos la máquina y nos pedirá seleccionar un disco de inicio. En este momento es cuando tenemos que seleccionar la imagen de Ubuntu Server 18.04.5 que nos hemos descargado y presionar en *Start*.

6. En la configuración inicial de Ubuntu, estableceremos el idioma y distribución de teclado que deseemos y dejaremos el resto de opciones tal y como vienen por defecto. Cuando lleguemos a la configuración de nuestro perfil, es necesario que el nombre del usuario sea *server*. Para la contraseña y el nombre del equipo no hay ningún tipo de restricción. Es importante rechazar cualquier tipo de actualización si se nos pidiese. Una vez finalizada la instalación se activará un botón para poder reiniciar la máquina.

7. Una vez reiniciada la máquina, iniciaremos sesión y ejecutaremos los siguientes comandos (es MUY importante ejecutar el último comando como superusuario):

```bash
sudo apt update
sudo apt install git mysql-server apache2 python3 python3-pip python3-venv libapache2-mod-wsgi-py3 php libapache2-mod-php
git clone https://github.com/fjdcordon/tfg-servidorweb
cd tfg-servidorweb
sudo ./setup.sh
```
8. Una vez finalizada la puesta en marcha del servidor web, la máquina se reiniciará de nuevo. Cuando vuelva a arrancar tendremos el componente totalmente funcional. Para entrar a la web desde nuestro ordenador anfitrión, abriremos el navegador e introduciremos la siguiente url: https://<ip de la máquina>:8443. Nos aparecerá una advertencia porque el certificado es autofirmado, pero pulsaremos en continuar. En este momento, debería aparecer por pantalla la página de inicio de sesión. Si ponemos las credenciales por defecto *user* y *password*, entraremos al monitor de control.

Es MUY importante destacar que el monitor nos dará un error de carga de datos y no funcionará si alguno de los otros dos componentes (PLC-SIM y Gateway IoT) no está encendido.
