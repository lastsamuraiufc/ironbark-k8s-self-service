import os

from flask import Flask, url_for, render_template, jsonify, request, redirect
from kubernetes import config , client
from kubernetes.client import Configuration
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
        try:
            config.load_kube_config()
            c = Configuration().get_default_copy()
        except AttributeError:
            c = Configuration()
            c.assert_homename = False
        Configuration.set_default(c)
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

        return redirect(url_for('namespaces'))

    @app.route('/namespaces')
    def namespaces():        

        # Enter a context with an instance of the API kubernetes.client
        api_instance = client.CoreV1Api()
        try:
            api_response = api_instance.list_namespace()
            metadata = api_response.items
            return render_template('namespaces_index.html', namespaces=metadata)
        except ApiException as e:
            print("Exception when calling CoreV1Api->create_namespace: %s\n" % e)

        return redirect(url_for('namespaces'))



    @app.route('/namespace/create', methods=["POST", "GET"])
    def namespace_add():
        
        if request.method == 'POST':
            # Enter a context with an instance of the API kubernetes.client
            api_instance = client.CoreV1Api()
            try:
                meta = client.V1ObjectMeta(name=request.form["namespaceName"])
                body = client.V1Namespace(metadata=meta) # V1Namespace | 
                api_response = api_instance.create_namespace(body)
            except ApiException as e:
                print("Exception when calling CoreV1Api->create_namespace: %s\n" % e)
            return redirect(url_for('namespaces'))

        return render_template('namespaces_add.html')

    return app
