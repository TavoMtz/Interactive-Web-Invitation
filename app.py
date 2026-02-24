from flask import Flask, render_template, request, jsonify
import sqlite3



app = Flask(__name__)

def init_db():
    conexion = sqlite3.connect('boda.db')
    cursor = conexion.cursor()
    cursor.execute('''
                CREATE TABLE IF NOT EXISTs invitados(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nombre VARCHAR(60) NOT NULL,
                   asistencia TEXT NOT NULL,
                   mensaje TEXT)
                   ''')
    conexion.commit()
    conexion.close()

init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/confirmar', methods=['POST'])
def confirmarInvitados():
    #Atrapar los valores del front en el python
    nombre_invitado = request.form.get('nombre')
    asistencia_invitado = request.form.get('asistencia')
    mensaje_invitado = request.form.get('mensaje')
    
    #Abrir la conexion a la base de datos
    conexion = sqlite3.connect('boda.db')
    cursor = conexion.cursor()
    #Revisa que no se haya registrado el usuario
    cursor.execute('SELECT * FROM invitados WHERE nombre = ?', (nombre_invitado,))
    invitado_existente = cursor.fetchone()
    if invitado_existente:
        return render_template('confirmado.html')
    else: 
        #Inserta a la gente en la base de datos 
        cursor.execute('''
                    INSERT INTO invitados(nombre, asistencia, mensaje) 
                    values (?, ?, ?)
                    ''', (nombre_invitado, asistencia_invitado, mensaje_invitado))
        conexion.commit()
        conexion.close()
        return render_template('gracias.html')

if __name__ == '__main__':
    app.run(debug=True)




