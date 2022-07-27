import os
from flask import Flask, render_template
import pulumi.automation as auto
from dotenv import dotenv_values

config = dotenv_values(".env")

def ensure_plugins():
    ws = auto.LocalWorkspace()
    ws.install_plugin("aws", "v4.0.0")

def create_app():
    ensure_plugins()
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=config['PULUMITOKEN'],
        PROJECT_NAME="ahi-service-starter",
        PULUMI_ORG="hantswilliams",
    )

    @app.route("/", methods=["GET"])
    def index():
        return render_template("index.html")

    import virtual_machines

    app.register_blueprint(virtual_machines.bp)

    return app