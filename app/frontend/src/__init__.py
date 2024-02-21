import os
from flask import Flask, url_for, render_template, jsonify, request

def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_mapping(
        TEMPLATES_AUTO_RELOAD = True
    )

    if test_config is None:
        # Load configuration from config.py
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404

    @app.route('/healthz')
    def healthz():
        return jsonify({}), 200

    @app.route('/readyz')
    def readyz():
        return jsonify({}), 200

    @app.route('/version')
    def version():
        return os.environ.get('APP_VERSION', default='dev'), 200

    @app.route('/')
    def index():

        return render_template('namespace.html')

    @app.route('/namespace/create', methods=["POST", "GET"])
    def namespace_add():
        
        if request.method == 'POST':
            namespace_file = open('namespace.txt', 'w')
            namespace_file.write(request.form["namespaceName"] + ',' + request.form["resourceLimits"] + ',' + request.form["resourceRequests"] + ',' + request.form["ownerEmail"])
            namespace_file.close()

        return render_template('namespace.html')

    return app