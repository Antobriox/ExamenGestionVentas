from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345@localhost/tiendaLinea'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Modelos de datos
class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)

class Vendedor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    region = db.Column(db.String(100), nullable=False)

class Venta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    producto_id = db.Column(db.Integer, db.ForeignKey('producto.id'), nullable=False)
    vendedor_id = db.Column(db.Integer, db.ForeignKey('vendedor.id'), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    fecha_venta = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    producto = db.relationship('Producto', backref=db.backref('ventas', lazy=True))
    vendedor = db.relationship('Vendedor', backref=db.backref('ventas', lazy=True))

# Rutas
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/productos')
def productos_index():
    productos = Producto.query.all()
    return render_template('productos_index.html', productos=productos)

@app.route('/productos/nuevo', methods=['GET', 'POST'])
def productos_form():
    if request.method == 'POST':
        nombre = request.form['nombre']
        precio = float(request.form['precio'])
        stock = int(request.form['stock'])
        producto = Producto(nombre=nombre, precio=precio, stock=stock)
        db.session.add(producto)
        db.session.commit()
        return redirect(url_for('productos_index'))
    return render_template('productos_form.html')

@app.route('/productos/editar/<int:id>', methods=['GET', 'POST'])
def productos_edit(id):
    producto = Producto.query.get_or_404(id)
    if request.method == 'POST':
        producto.nombre = request.form['nombre']
        producto.precio = float(request.form['precio'])
        producto.stock = int(request.form['stock'])
        db.session.commit()
        return redirect(url_for('productos_index'))
    return render_template('productos_form.html', producto=producto)

@app.route('/productos/eliminar/<int:id>')
def productos_delete(id):
    producto = Producto.query.get_or_404(id)
    db.session.delete(producto)
    db.session.commit()
    return redirect(url_for('productos_index'))

@app.route('/vendedores')
def clientes_index():
    vendedores = Vendedor.query.all()
    return render_template('clientes_index.html', vendedores=vendedores)

@app.route('/vendedores/nuevo', methods=['GET', 'POST'])
def clientes_form():
    if request.method == 'POST':
        nombre = request.form['nombre']
        region = request.form['region']
        vendedor = Vendedor(nombre=nombre, region=region)
        db.session.add(vendedor)
        db.session.commit()
        return redirect(url_for('clientes_index'))
    return render_template('clientes_form.html')

@app.route('/vendedores/editar/<int:id>', methods=['GET', 'POST'])
def clientes_edit(id):
    vendedor = Vendedor.query.get_or_404(id)
    if request.method == 'POST':
        vendedor.nombre = request.form['nombre']
        vendedor.region = request.form['region']
        db.session.commit()
        return redirect(url_for('clientes_index'))
    return render_template('clientes_form.html', vendedor=vendedor)

@app.route('/vendedores/eliminar/<int:id>')
def clientes_delete(id):
    vendedor = Vendedor.query.get_or_404(id)
    db.session.delete(vendedor)
    db.session.commit()
    return redirect(url_for('clientes_index'))

@app.route('/ventas')
def ventas_index():
    ventas = Venta.query.all()
    return render_template('ventas_index.html', ventas=ventas)

@app.route('/ventas/nuevo', methods=['GET', 'POST'])
def ventas_form():
    productos = Producto.query.all()
    vendedores = Vendedor.query.all()
    if request.method == 'POST':
        producto_id = int(request.form['producto_id'])
        vendedor_id = int(request.form['vendedor_id'])
        cantidad = int(request.form['cantidad'])
        fecha_venta = datetime.strptime(request.form['fecha_venta'], '%Y-%m-%d')
        venta = Venta(producto_id=producto_id, vendedor_id=vendedor_id, cantidad=cantidad, fecha_venta=fecha_venta)
        db.session.add(venta)
        db.session.commit()
        return redirect(url_for('ventas_index'))
    return render_template('ventas_form.html', productos=productos, vendedores=vendedores)

@app.route('/ventas/editar/<int:id>', methods=['GET', 'POST'])
def ventas_edit(id):
    venta = Venta.query.get_or_404(id)
    productos = Producto.query.all()
    vendedores = Vendedor.query.all()
    if request.method == 'POST':
        venta.producto_id = int(request.form['producto_id'])
        venta.vendedor_id = int(request.form['vendedor_id'])
        venta.cantidad = int(request.form['cantidad'])
        venta.fecha_venta = datetime.strptime(request.form['fecha_venta'], '%Y-%m-%d')
        db.session.commit()
        return redirect(url_for('ventas_index'))
    return render_template('ventas_form.html', venta=venta, productos=productos, vendedores=vendedores)

@app.route('/ventas/eliminar/<int:id>')
def ventas_delete(id):
    venta = Venta.query.get_or_404(id)
    db.session.delete(venta)
    db.session.commit()
    return redirect(url_for('ventas_index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)