from flask import Flask, render_template, request, redirect, url_for
# Initialize the Flask application
from flask import Response, Flask, request
import prometheus_client
from prometheus_client.core import CollectorRegistry
from prometheus_client import Summary, Counter, Histogram, Gauge
import time

app = Flask(__name__)


_INF = float("inf")

graphs = {}
graphs['t'] = Counter('python_login_requests_total', 'The total number of processed login requests')
graphs['er'] = Counter('python_error_percentage', 'Error Percentage of login requests')
graphs['cp'] = Counter('python_cpu_utilization', 'Cpu utilization')
graphs['s'] = Counter('python_login_requests_processed', 'The total number of successful login requests')
graphs['f'] = Counter('python_login_requests_failed', 'The total number of failed login requests')
graphs['h'] = Histogram('python_request_duration_seconds', 'Histogram for the duration in seconds.', buckets=(1, 2, 3, _INF))


@app.route('/')
def index():
   start = time.time()
   graphs['t'].inc()
   toal=graphs['t']
   
   time.sleep(0.600)
   end = time.time()
   graphs['h'].observe(end - start)
   return render_template("log_in.html")

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST' and request.form['txtemail'] == 'vamshi@kubernetes.com' and request.form['txtpass'] == 'vamshi' :
      return redirect(url_for('success'))
   else:
      return redirect(url_for('errorlogin'))

@app.route('/success')
def success():
   start = time.time()
   graphs['s'].inc()

   time.sleep(0.500)
   end = time.time()
   graphs['h'].observe(end - start)
   return '<h1>logged in successfully</h1>'

@app.route('/errorlogin')
def errorlogin():
   start = time.time()
   graphs['f'].inc()
   err=graphs['f']
   
   toal = graphs['t']
   toal1=int(toal)
   errp=toal1*100
   graphs['er']=errp
   time.sleep(0.800)
   end = time.time()
   graphs['h'].observe(end - start)
   return '<h1>Bad Credentials. Please login again <a href = "/">login</a></h1>'

@app.route("/metrics")
def requests_count():


    graph['cp']=psutil.cpu_percent(4)

    res = []
    for k,v in graphs.items():
        res.append(prometheus_client.generate_latest(v))
    return Response(res, mimetype="text/plain")

if __name__ == '__main__':
   app.run(debug = True, host='0.0.0.0')

