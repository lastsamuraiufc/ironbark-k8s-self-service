import os

from flask import Flask, url_for, render_template, jsonify, request, redirect
import kubernetes.client
from kubernetes.client.rest import ApiException
import requests
import logging
import json
from pprint import pprint

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
        return render_template('namespaces_index.html', namespaces=metadata)

    @app.route('/namespace/create', methods=["POST", "GET"])
    def namespace_add():
        
        if request.method == 'POST':
            configuration = kubernetes.client.Configuration()
            configuration.host = app.config['API_URL']
            # Enter a context with an instance of the API kubernetes.client
            with kubernetes.client.ApiClient(configuration) as api_client:
                # Create an instance of the API class
                api_instance = kubernetes.client.CoreV1Api(api_client)
                meta = kubernetes.client.V1ObjectMeta(name=request.form["namespaceName"])
                print(meta)
                body = kubernetes.client.V1Namespace(metadata=meta) # V1Namespace | 

                try:
                    api_response = api_instance.create_namespace(body)
                    pprint(api_response)
                except ApiException as e:
                    print("Exception when calling CoreV1Api->create_namespace: %s\n" % e)
                return redirect(url_for('namespaces'))

        return render_template('namespaces_add.html')

    return app
