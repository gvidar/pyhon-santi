from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
app =  Flask(__name__)
app.config['MYSQL_HOST']='Localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='Vidarte1511'
app.config['MYSQL_DB']='mecon'
app.config['MYSQL_PORT'] = 3306
mysql = MySQL(app)

app.secret_key = 'meconkey'
 


@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM requerimientos')
    data = cur.fetchall()
    return render_template ('index.html', requerimientos = data)

@app.route('/agregar_info', methods=['POST'])
def agregar_info():
    n_servicio = request.form['n_servicio']
    id_jur = request.form['id_jur']
    ff = request.form['ff']
    objeto = request.form['objeto']
    rubro = request.form['rubro']
    credito = request.form['credito']
    smp = request.form['smp']
    expediente = request.form['expediente']
    recurso = request.form['recurso']
    observaciones = request.form['observaciones']
    sql = 'INSERT INTO requerimientos (n_servicio,id_jur,ff,objeto,rubro, credito, smp, expediente, recurso, observaciones ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s,%s)'
    values = (n_servicio,id_jur,ff,objeto,rubro, credito, smp, expediente, recurso, observaciones)
    cur = mysql.connection.cursor()
    cur.execute(sql, values)
    mysql.connection.commit()
    flash('Se generó un nuevo registro')
    
    return redirect(url_for('Index'))

@app.route('/edit/<id>')
def edit_info(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM requerimientos WHERE id = {0}'.format(id))
    data = cur.fetchall()
    print(data[0])
    return render_template('edit.html', requerimiento = data[0])

@app.route('/update/<int:id>', methods = ['POST'])
def update_info(id):
    if request.method == 'POST':
        n_servicio = request.form['n_servicio']   
        id_jur = request.form['id_jur']
        ff = request.form['ff']
        objeto = request.form['objeto']
        rubro = request.form['rubro']
        credito = request.form['credito']
        smp = request.form['smp']
        expediente = request.form['expediente']
        recurso = request.form['recurso']
        observaciones = request.form['observaciones']
    cur = mysql.connection.cursor()
    cur.execute("""
    UPDATE requerimientos
    SET n_servicio = %s,
    id_jur = %s,
    ff = %s,
    objeto = %s,
    rubro = %s,
    credito = %s,
    smp = %s,
    expediente = %s,
    recurso = %s,
    observaciones = %s,
    WHERE id=%s
    """,(n_servicio,id_jur,ff,objeto,rubro,credito,smp,expediente,recurso,observaciones,id))
    mysql.connection.commit()
    flash('Actualizado correctamente')
    return redirect(url_for('index.html'))

@app.route('/delete/<string:id>')
def delete_inf(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM requerimientos WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('Dato eliminado')
    return redirect(url_for('Index'))
   

if __name__=='__main__':
 
    app.run(debug=True) 
#commit