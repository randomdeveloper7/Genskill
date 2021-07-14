from flask import Flask, render_template, request
from pi_estimators import monte_carlo, wallis 

app = Flask("PI")

@app.route("/")
def intro():
    return render_template("pi_main.html")

@app.route("/estimate", methods=["POST"]) #request usually uses "get" method but here we need "post" method
def estimate():
    algorithm = request.form['Algorithm']   #we can get the value of the algorithm (mc or w as specified in pi_base.html) from html forms using the name of the input i.e, here name = "Algorithm" in the html code. So to get the  we use request.form['Algorithm']
    iterations = request.form['Iterations']
    if(algorithm == "mc"):
        estimate = monte_carlo(int(iterations))
    else:
        estimate = wallis(int(iterations))
    
    algos = {"mc" : "Monte Carlo Estimation", "w" : "Wallis Product"}
    
    return render_template("pi_estimate.html", heading = algos[algorithm], iters = iterations, estimate = estimate)

if(__name__ == "__main__"):
    app.run()