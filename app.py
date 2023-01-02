from flask import Flask, request, render_template


app = Flask(__name__,template_folder='templates')

@app.route("/",methods=['GET','POST'])
def price_predictor():
    if request.method == 'POST':
        area=request.form['area']
        bhk=request.form['bhk']
        return area+bhk
    return render_template('predict.html')

if __name__ == "__main__":
    app.run(debug=True)