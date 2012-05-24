from barcodes import app

if app.debug:
    app.run(host='0.0.0.0')
else:
    app.run()
