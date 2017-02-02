from flask import Flask
from redis import Redis
from prometheus_client import Counter, start_http_server

app = Flask(__name__)
redis = Redis(host="192.168.99.100", port=30001)
counter = Counter('total_requests', 'Number of requests counter')
start_http_server(9090)

@app.route("/")
def hello():
    counter.inc()
    visits = redis.incr('counter')
    html = "<h3>Hello World!</h3>" \
           "<b>Visits:</b> {visits}" \
           "<br/>"
    return html.format(visits=visits)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
