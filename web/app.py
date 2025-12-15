from flask import Flask, render_template_string
import subprocess

SERVERS = [
    ("Phobos", "quake-phobos", 27500),
    ("Deimos", "quake-deimos", 27501),
]

app = Flask(__name__)

TEMPLATE = """
<!doctype html>
<html>
<head>
  <title>K8 Quake Servers</title>
  <meta http-equiv="refresh" content="5">
  <style>
    body { font-family: monospace; background:#111111; color:#eeeeee;}
    .online { color: #00ff00; }
    .offline { color: #ff0000; }
  </style>
</head>
<body>
  <h1>Quake Servers</h1>
  {% for s in servers %}
    <h2>{{ s.name }}</h2>
    <pre class="{{ 'offline' if 'no response' in s.output.lower() else 'online' }}">
{{ s.output }}
    </pre>
  {% endfor %}
</body>
</html>
"""

def query_server(host, port):
    cmd = ["quakestat", "-qws", f"{host}:{port}"]
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT, universal_newlines=True)
    except subprocess.CalledProcessError as e:
        output = e.output
    except Exception as e:
        output = f"Error running quakestat: {e}"
    return output

@app.route("/")
def index():
    statuses = []
    for name, host, port in SERVERS:
        statuses.append({
            "name": name,
            "output": query_server(host, port),
        })
    return render_template_string(TEMPLATE, servers=statuses)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
