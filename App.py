############# importar librerias o recursos#####
from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin

# initializations
app = Flask(__name__)
CORS(app)

# Mysql Connection
app.config['MYSQL_HOST'] = 'localhost' 
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'prestamos'
mysql = MySQL(app)

# settings A partir de ese momento Flask utilizará esta clave para poder cifrar la información de la cookie
app.secret_key = "mysecretkey"






#### ruta para crear un registro cliente########
@cross_origin()
@app.route('/add_clientes', methods=['POST'])
def add_clientes():
    if request.method == 'POST':
        tipo_documento = request.json['tipo_documento']  ## Tipo documento
        num_documento = request.json['num_documento']  ## Numero documento
        nombre_completo = request.json['nombre_completo']  ## nombre completo
        telefono = request.json['telefono']        ## telefono        
        direccion = request.json['direccion']  ## direccion
        email = request.json['email']        ## email
        ocupacion = request.json['ocupacion']  ## ocupacion
        tipo_contrato = request.json['tipo_contrato']  ## Tipo contrato
        antiguedad_laboral = request.json['antiguedad_laboral']  ## Antiguedad laboral
        tipo_vivienda = request.json['tipo_vivienda']  ## Tipo vivienda
        ingreso_mensual = request.json['ingreso_mensual']  ## Ingreso mensual 
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO clientes (tipo_documento, num_documento, nombre_completo, telefono, direccion, email, ocupacion, tipo_contrato, antiguedad_laboral, tipo_vivienda, ingreso_mensual) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (tipo_documento, num_documento, nombre_completo,telefono,direccion,email, ocupacion, tipo_contrato, antiguedad_laboral, tipo_vivienda, ingreso_mensual))
        mysql.connection.commit()
        return jsonify({"informacion":"Registro exitoso"})


######### ruta para actualizar clientes################
@cross_origin()
@app.route('/update_clientes/<id_cliente>', methods=['PUT'])
def update_clientes(id_cliente):
    tipo_documento = request.json['tipo_documento']  ## Tipo documento
    num_documento = request.json['num_documento']  ## Numero documento
    nombre_completo = request.json['nombre_completo']  ## nombre completo
    telefono = request.json['telefono']        ## telefono        
    direccion = request.json['direccion']  ## direccion
    email = request.json['email']        ## email
    ocupacion = request.json['ocupacion']  ## ocupacion
    tipo_contrato = request.json['tipo_contrato']  ## Tipo contrato
    antiguedad_laboral = request.json['antiguedad_laboral']  ## Antiguedad laboral
    tipo_vivienda = request.json['tipo_vivienda']  ## Tipo vivienda
    ingreso_mensual = request.json['ingreso_mensual']  ## Ingreso mensual    
    cur = mysql.connection.cursor()
    cur.execute("""
        UPDATE clientes
        SET tipo_documento = %s,
            num_documento = %s,
            nombre_completo = %s,           
            telefono = %s,
            direccion = %s,
            email = %s,
            ocupacion = %s,
            tipo_contrato = %s,
            antiguedad_laboral = %s,
            tipo_vivienda = %s,
            ingreso_mensual = %s
        WHERE id_cliente = %s
    """, (tipo_documento, num_documento, nombre_completo,telefono,direccion,email, ocupacion, tipo_contrato, antiguedad_laboral, tipo_vivienda, ingreso_mensual, id_cliente))
    mysql.connection.commit()
    return jsonify({"informacion":"Registro actualizado"})


##### ruta para consultar todos los registros clientes#####
@cross_origin()
@app.route('/getAll_clientes', methods=['GET'])
def getAll_clientes():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM clientes')
    rv = cur.fetchall()
    cur.close()
    payload = []
    content = {}
    for result in rv:
       content = {'id_cliente': result[0], 'tipo_documento':result[1], 'num_documento':result[2], 'nombre_completo':result[3],'telefono':result[4],'direccion':result[5],'email':result[6], 'ocupacion':result[7], 'tipo_contrato':result[8], 'antiguedad_laboral':result[9], 'tipo_vivienda':result[10], 'ingreso_mensual':result[11]}
       payload.append(content)
       content = {}
    return jsonify(payload)



###ruta para consultar por parametro cliente#####
@cross_origin()
@app.route('/getAllById_clientes/<id_cliente>',methods=['GET'])
def getAllById_clientes(id_cliente):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM clientes WHERE id_cliente = %s', (id_cliente))
    rv = cur.fetchall()
    cur.close()
    payload = []
    content = {}
    for result in rv:
        content = {'id_cliente': result[0], 'tipo_documento':result[1], 'num_documento':result[2], 'nombre_completo':result[3],'telefono':result[4],'direccion':result[5],'email':result[6], 'ocupacion':result[7], 'tipo_contrato':result[8], 'antiguedad_laboral':result[9], 'tipo_vivienda':result[10], 'tipo_ingreso_mensual':result[11], 'id_cliente':result[12]}
        payload.append(content)
        content = {}
    return jsonify(payload)


#### eliminar registro clientes####
@cross_origin()
@app.route('/delete_clientes/<id_cliente>', methods = ['DELETE'])
def delete_clientes(id_cliente):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM clientes WHERE id_cliente = %s', (id_cliente,))
    mysql.connection.commit()
    return jsonify({"informacion":"Registro eliminado"})


#### ruta para crear un registro pagos########
@cross_origin()
@app.route('/add_pagos', methods=['POST'])
def add_pagos():
    if request.method == 'POST':
        codigo_pago = request.json['codigo_pago'] ## codigo_pago
        valor_pago = request.json['valor_pago'] ## valor_pago
        fecha_pago = request.json['fecha_pago']  ## fecha_pago
        estado = request.json['estado']  ## estado
        id_prestamo = request.json['id_prestamo']  ## id_prestamo
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO pagos (codigo_pago, valor_pago, fecha_pago, estado, id_prestamo) VALUES (%s,%s,%s,%s,%s)", (codigo_pago, valor_pago, fecha_pago, estado, id_prestamo))
        mysql.connection.commit()
        return jsonify({"informacion":"Registro exitoso"})



######### ruta para actualizar pagos################
@cross_origin()
@app.route('/update_pagos/<id_pago>', methods=['PUT'])
def update_pagos(id_pago):
    codigo_pago = request.json['codigo_pago'] ## codigo_pago
    valor_pago = request.json['valor_pago'] ## valor_pago
    fecha_pago = request.json['fecha_pago']  ## fecha_pago
    estado = request.json['estado']  ## estado
    id_prestamo = request.json['id_prestamo']  ## id_prestamo
    cur = mysql.connection.cursor()
    cur.execute("""
        UPDATE pagos
        SET codigo_pago = %s,
            valor_pago = %s,
            fecha_pago = %s,
            estado = %s,
            id_prestamo = %s
        WHERE id_pago = %s
    """, (codigo_pago, valor_pago, fecha_pago, estado, id_prestamo, id_pago))
    mysql.connection.commit()
    return jsonify({"informacion":"Registro actualizado"})


##### ruta para consultar todos los registros pagos#####
@cross_origin()
@app.route('/getAll_pagos', methods=['GET'])
def getAll_pagos():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM pagos')
    rv = cur.fetchall()
    cur.close()
    payload = []
    content = {}
    for result in rv:
       content = {'id_pago': result[0], 'codigo_pago': result[1], 'valor_pago': result[2], 'fecha_pago': result[3], 'estado': result[4], 'id_prestamo': result[5]}
       payload.append(content)
       content = {}
    return jsonify(payload)


###ruta para consultar por parametro pagos#####
@cross_origin()
@app.route('/getAllById_pagos/<id_pago>',methods=['GET'])
def getAllById_pagos(id_pago):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM pagos WHERE id_pago = %s', (id_pago))
    rv = cur.fetchall()
    cur.close()
    payload = []
    content = {}
    for result in rv:
       content = {'id_pago': result[0], 'codigo_pago': result[1], 'valor_pago': result[2], 'fecha_pago': result[3], 'estado': result[4], 'id_prestamo': result[5]}
       payload.append(content)
       content = {}
    return jsonify(payload)


#### eliminar registro pagos####
@cross_origin()
@app.route('/delete_pagos/<id_pago>', methods = ['DELETE'])
def delete_pagos(id_pago):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM pagos WHERE id_pago = %s', (id_pago,))
    mysql.connection.commit()
    return jsonify({"informacion":"Registro eliminado"})


#### ruta para crear un registro prestamos########
@cross_origin()
@app.route('/add_creditos', methods=['POST'])
def add_creditos():
    if request.method == 'POST':
        codigo_prestamo = request.json['codigo_prestamo']  ## codigo_prestamo
        valor_prestamo = request.json['valor_prestamo']  ## valor_prestamo
        num_cuotas = request.json['num_cuotas']  ## numero de cuotas
        meses_plazo = request.json['meses_plazo'] ## meses_plazo
        fecha_inicio_prestamo = request.json['fecha_inicio_prestamo']  ## fecha inicio prestamo
        fecha_final_prestamo = request.json['fecha_final_prestamo']  ## fecha final prestamo
        intereses = request.json['intereses']  ## intereses
        valor_final_prestamo = request.json['valor_final_prestamo']  ## valor_final_prestamo
        estado = request.json['estado']  ## estado
        id_cliente = request.json['id_cliente']  ## id_cliente
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO prestamo (codigo_prestamo, valor_prestamo, num_cuotas, meses_plazo, fecha_inicio_prestamo, fecha_final_prestamo, intereses, valor_final_prestamo, estado, id_cliente) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (codigo_prestamo,valor_prestamo, num_cuotas, meses_plazo, fecha_inicio_prestamo, fecha_final_prestamo, intereses, valor_final_prestamo, estado, id_cliente))
        mysql.connection.commit()
        return jsonify({"informacion":"Registro exitoso"})


######### ruta para actualizar prestamos################
@cross_origin()
@app.route('/update_creditos/<id_prestamo>', methods=['PUT'])
def update_creditos(id_prestamo):
    codigo_prestamo = request.json['codigo_prestamo']  ## codigo_prestamo
    valor_prestamo = request.json['valor_prestamo']  ## valor_prestamo
    num_cuotas = request.json['num_cuotas']  ## numero de cuotas
    meses_plazo = request.json['meses_plazo'] ## meses_plazo
    fecha_inicio_prestamo = request.json['fecha_inicio_prestamo']  ## fecha inicio prestamo
    fecha_final_prestamo = request.json['fecha_final_prestamo']  ## fecha final prestamo
    intereses = request.json['intereses']  ## intereses
    valor_final_prestamo = request.json['valor_final_prestamo']  ## valor_final_prestamo
    estado = request.json['estado']  ## estado
    id_cliente = request.json['id_cliente']  ## id_cliente
    cur = mysql.connection.cursor()
    cur.execute("""
        UPDATE prestamo
        SET codigo_prestamo = %s,
            valor_prestamo = %s,
            num_cuotas = %s,
            meses_plazo = %s,
            fecha_inicio_prestamo = %s,
            fecha_final_prestamo = %s,
            intereses = %s,
            valor_final_prestamo = %s,
            estado = %s,
            id_cliente = %s
        WHERE id_prestamo = %s
    """, (codigo_prestamo, valor_prestamo, num_cuotas, meses_plazo, fecha_inicio_prestamo, fecha_final_prestamo, intereses, valor_final_prestamo, estado, id_cliente, id_prestamo))
    mysql.connection.commit()
    return jsonify({"informacion":"Registro actualizado"})



##### ruta para consultar todos los registros prestamos#####
@cross_origin()
@app.route('/getAll_creditos', methods=['GET'])
def getAll_creditos():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM prestamo')
    rv = cur.fetchall()
    cur.close()
    payload = []
    content = {}
    for result in rv:
       content = {'id_prestamo': result[0], 'codigo_prestamo': result[1], 'valor_prestamo': result[2], 'num_cuotas': result[3], 'meses_plazo': result[4], 'fecha_inicio_prestamo': result[5], 'fecha_final_prestamo': result[6], 'intereses': result[7], 'valor_final_prestamo': result[8], 'estado': result[9], 'id_cliente': result[10]}
       payload.append(content)
       content = {}
    return jsonify(payload)


###ruta para consultar por parametro prestamos#####
@cross_origin()
@app.route('/getAllById_creditos/<id_prestamo>',methods=['GET'])
def getAllById_creditos(id_prestamo):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM prestamo WHERE id_prestamo = %s', (id_prestamo))
    rv = cur.fetchall()
    cur.close()
    payload = []
    content = {}
    for result in rv:
       content = {'id_prestamo': result[0], 'codigo_prestamo': result[1], 'valor_prestamo': result[2], 'num_cuotas': result[3], 'meses_plazo': result[4], 'fecha_inicio_prestamo': result[5], 'fecha_final_prestamo': result[6], 'intereses': result[7], 'valor_final_prestamo': result[8], 'estado': result[9], 'id_cliente': result[10]}
       payload.append(content)
       content = {}
    return jsonify(payload)


    #### eliminar registro prestamos####
@cross_origin()
@app.route('/delete_creditos/<id_prestamo>', methods = ['DELETE'])
def delete_creditos(id_prestamo):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM prestamo WHERE id_prestamo = %s', (id_prestamo,))
    mysql.connection.commit()
    return jsonify({"informacion":"Registro eliminado"})


@cross_origin()
@app.route('/login',methods=['GET'])
def login():
    user = request.json['user']
    password = request.json['password']
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM user WHERE user = %s and password =%s", (user,password))
    ###cur.execute('SELECT * FROM empleados')
    data = cur.fetchall()
    cur.close()
    print("enviado")
   
    if len(data)==0 :
        return jsonify({"data":0})
    else :
        return jsonify({"data":data})

# starting the app
if __name__ == "__main__":
    app.run(port=3000, debug=True)        