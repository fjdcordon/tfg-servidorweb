Servidor web de monitorización y control de una instalación fotovoltaica
=============

Este servidor web es uno de los componentes del escenario que se ha puesto en marcha para la realización de una prueba de concepto que tiene como objetivo analizar las posibilidades de explotación de vulnerabilidades en entornos del Internet Industrial de las Cosas (IIoT, de su acepción en Inglés). Este escenario está compuesto además por otros dos elementos: un componente OT, una simulación de un PLC industrial real (PLC-SIM); y un componente IoT, un gateway IoT que hace de interfaz IT/OT.

Para más información sobre el desarrollo de este escenario y la verificación de esta prueba de concepto se puede consultar mi Trabajo de Fin de Grado: «Análisis y explotación de vulnerabilidades en un sistema de monitorización y control remoto de energía solar».

Autor: Francisco Javier Domínguez Cordón

Instalación
-------------

1. Descargar la imagen ISO de Ubuntu Server 18.04.5: [Descargar Imagen](https://old-releases.ubuntu.com/releases/18.04.5/ubuntu-18.04-live-server-amd64.iso)
2. Dado que la infraestructura está virtualizada, hay que descargar un software de virtualización. En este caso, se ha optado por utilizar [Oracle VM VirtualBox](https://www.virtualbox.org/), un software de código abierto, gratuito y multiplataforma (Windows, GNU/Linux, Mac OS). Para instalarlo simplemente hay que seguir los pasos que se detallan en su página web.
3. Una vez instalado, lo abrimos y pulsamos sobre el botón *New* o *Nueva* (dependiendo del idioma en que este configurado el equipo anfitrión). Pondremos el nombre que deseemos a la máquina, indicaremos que se trata de un Linux y que la distribución es Ubuntu (64-bit). Dejaremos el resto de la configuración por defecto.

![](https://github.com/fjdcordon/tfg-servidorweb/blob/master/images/instalacion1.png)

![](https://github.com/fjdcordon/tfg-servidorweb/blob/master/images/instalacion2.png)

4. Una vez hecha la primera configuración de la máquina, vamos cambiar los ajustes de red. Para ello, hacemos click sobre la máquina y presionamos *Settings* o *Configuración*. Nos vamos a la opción de *Network* o *Red* y configuraremos el primer adaptador como *Bridged Adapter* o *Adaptador Puente* y el segundo adaptador como *Internal Network* o *Red Interna*. El nombre de la red interna será *intnet*.

![](https://github.com/fjdcordon/tfg-servidorweb/blob/master/images/instalacion3.png)

![](https://github.com/fjdcordon/tfg-servidorweb/blob/master/images/instalacion4.png)

5.
