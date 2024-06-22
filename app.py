from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/formulario",methods=["GET","POST"])
def formulario():
    if request.method == "POST":
        A = request.form["datoA"]
        B = request.form["datoB"]
        #print(int(A)+int(B))
        C = int(A) + int(B)
        
        return render_template("formulario.html",C=C,A=A,B=B)
    return render_template("formulario.html")

if __name__=="__main__":
    app.run()