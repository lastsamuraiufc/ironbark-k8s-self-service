import os

from flask import Flask, url_for, render_template, jsonify, request, redirect
import requests
import logging
import json

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

        return render_template('namespaces_index.html')

    @app.route('/namespaces')
    def namespaces():        

        response_API = requests.get(app.config['API_URL'] + '/api/v1/namespaces')
        data = json.loads(response_API.text)
        metadata = data['items']
        for key in metadata:
            print(key, " : ", key['metadata'])
        return render_template('namespaces_index.html', namespaces=metadata)

    @app.route('/namespace/create', methods=["POST", "GET"])
    def namespace_add():
        
        if request.method == 'POST':
            namespace_file = open('namespace.txt', 'w')
            namespace_file.write(request.form["namespaceName"] + ',' + request.form["resourceLimits"] + ',' + request.form["resourceRequests"] + ',' + request.form["ownerEmail"])
            namespace_file.close()

        return redirect(url_for('namespaces'))

    return app
    
