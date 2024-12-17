from flask import Flask, render_template, request, redirect, url_for


#hello from a new version

app = Flask(__name__)

# Lista de tareas, en una aplicación real esto se almacenaría en una base de datos
tareas = []

@app.route('/')
def index():
    return render_template('index.html', tareas=tareas)

@app.route('/agregar', methods=['GET', 'POST'])
def agregar_tarea():
    if request.method == 'POST':
        tarea = request.form['tarea']
        tareas.append({'tarea': tarea, 'completa': False})
        return redirect(url_for('index'))
    return render_template('agregar_tarea.html')

@app.route('/completar/<int:id>')
def completar_tarea(id):
    tareas[id]['completa'] = True
    return redirect(url_for('index'))

@app.route('/eliminar/<int:id>')
def eliminar_tarea(id):
    tareas.pop(id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
