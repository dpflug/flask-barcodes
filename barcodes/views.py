from barcodes import app, mail
from cStringIO import StringIO
from database import db_session
from flask import make_response, url_for, redirect
from flask import request, render_template, flash
from flaskext.mail import Message
from forms import RegistrationForm
from models import User
import barcode
import qrcode


@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()


@app.route('/', methods=['POST', 'GET'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(form.fullname.data, form.email.data)
        db_session.add(user)
        db_session.commit()
        msg = Message(
                'Here are your barcodes!',
                sender=('Barcode Generator', 'barcode_generator@example.org'),
                recipients=[form.email.data],
                body='Enjoy.'
            )
        msg.attach('code39.png', 'image/png', gen_code39(form.fullname.data))
        msg.attach('qr.png', 'image/png', gen_qr(form.fullname.data))
        mail.send(msg)
        flash('Thank you for registering! Your barcode is in your inbox.')
        return redirect(url_for('register'))
    return render_template('register.html', form=form)


@app.route('/code39/<uuid>')
def render_code39(uuid):
    response = make_response(gen_code39(uuid))
    response.headers["Content-type"] = "image/png"
    return response


@app.route('/ean13/<int:uuid>')
def render_ean13(uuid):
    response = make_response(gen_ean13(uuid))
    response.headers["Content-type"] = "image/png"
    return response


@app.route('/qr/<uuid>')
def render_qr(uuid):
    response = make_response(gen_qr(uuid))
    response.headers["Content-type"] = "image/png"
    return response


@app.route('/barcodes/<uuid>')
def barcode_sheet(uuid):
    try:
        int(uuid)
        uuidint = True
    except ValueError:
        uuidint = False

    return render_template('barcodes.html', uuid=uuid, uuidint=uuidint)


# Helper functions
def gen_qr(content):
    fp = StringIO()
    img = qrcode.make(content, box_size=5)
    img.save(fp)
    image = fp.getvalue()
    fp.close
    return image


def gen_code39(content):
    fp = StringIO()
    makepng = barcode.writer.ImageWriter()
    barcode.generate(
        'Code39',
        content,
        output=fp,
        writer=makepng,
    )
    image = fp.getvalue()
    fp.close()
    return image


def gen_ean13(content):
    try:
        int(content)
    except ValueError:
        return None

    fp = StringIO()
    notext = barcode.writer.ImageWriter()
    barcode.generate(
        'EAN13',
        str(content),
        output=fp,
        writer=notext
    )
    image = fp.getvalue()
    fp.close()
    return image
