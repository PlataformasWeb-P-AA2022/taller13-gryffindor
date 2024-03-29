import imp
from flask import Flask, render_template
import requests
import json
from config import user, passw

app = Flask(__name__, template_folder='templates')


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/losedificios")
def los_edificios():
    """
    """
    r = requests.get("http://127.0.0.1:8000/api/edificios/",
                     auth=(user, passw))
    edificios = json.loads(r.content)['results']
    numero_edificios = json.loads(r.content)['count']
    return render_template("losedificios.html", edificios=edificios,
                           numero_edificios=numero_edificios)


@app.route("/losdepartamentos")
def los_departamentos():
    """
    """
    r = requests.get("http://127.0.0.1:8000/api/departamentos/",
                     auth=(user, passw))
    datos = json.loads(r.content)['results']
    numero = json.loads(r.content)['count']
    return render_template("losdepartamentos.html", datos=datos,
                           numero=numero)


@app.route("/losdepartamentosdos")
def los_departamentos_dos():
    """
    """
    r = requests.get("http://127.0.0.1:8000/api/departamentos/",
                     auth=(user, passw))
    datos = json.loads(r.content)['results']
    numero = json.loads(r.content)['count']
    datos2 = []
    for d in datos:
        datos2.append({'propietario': d['propietario'], 'costo': d['costo'],
                       'edificio': obtener_edificio(d['edificio'])})
    return render_template("losdepartamentosdos.html", datos=datos2,
                           numero=numero)

# funciones ayuda


def obtener_edificio(url):
    """
    """
    r = requests.get(url, auth=(user, passw))
    nombre_edificio = json.loads(r.content)['nombre']
    dirreccion = json.loads(r.content)['direccion']
    ciudad = json.loads(r.content)['ciudad']
    cadena = "%s %s %s" % (nombre_edificio, dirreccion, ciudad)
    return cadena
