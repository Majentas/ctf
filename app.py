from flask import Flask, render_template, request, jsonify
import subprocess
import uuid
import socket
import atexit

app = Flask(__name__)

containers = {}

def find_available_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("", 0))
        return s.getsockname()[1]

def cleanup_all_containers():
    for container_name in containers.values():
        subprocess.run(f"docker rm -f {container_name}", shell=True)

@app.route("/")
def index():
    container_name = "ctf-container-" + str(uuid.uuid4())
    port = find_available_port()

    command = f"docker run -dit --name {container_name} majentas/debian-ctf1 /bin/bash"
    subprocess.run(command, shell=True)

    ttyd_command = f"ttyd -p {port} --writable docker exec -it {container_name} /bin/bash"
    subprocess.Popen(ttyd_command, shell=True)

    containers[port] = container_name

    return render_template("redirect.html", port=port)

@app.route("/cleanup", methods=["POST"])
def cleanup():
    port = request.json.get("port")
    container_name = containers.pop(port, None)
    if container_name:
        subprocess.run(f"docker rm -f {container_name}", shell=True)
        return jsonify({"status": "success"})
    return jsonify({"status": "container not found"}), 404

if __name__ == "__main__":
    atexit.register(cleanup_all_containers)
    app.run(debug=True)
