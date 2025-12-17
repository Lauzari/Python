from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)
ARCHIVO = "tareas.json"


def cargar_tareas():
    if not os.path.exists(ARCHIVO):
        return []

    with open(ARCHIVO, "r", encoding="utf-8") as f:
        return json.load(f)


def guardar_tareas(tareas):
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(tareas, f, indent=4, ensure_ascii=False)


@app.route("/")
def index():
    tareas = cargar_tareas()
    return render_template("index.html", tareas=tareas)


@app.route("/agregar", methods=["POST"])
def agregar():
    descripcion = request.form["descripcion"]
    tareas = cargar_tareas()
    tareas.append({"descripcion": descripcion, "completada": False})
    guardar_tareas(tareas)
    return redirect(url_for("index"))


@app.route("/completar/<int:indice>")
def completar(indice):
    tareas = cargar_tareas()
    tareas[indice]["completada"] = True
    guardar_tareas(tareas)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
