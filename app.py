from flask import Flask, request, render_template, redirect, url_for


app = Flask(__name__,template_folder='templates')
# global area
# area=None
@app.route("/",methods=['GET','POST'])
def price_predictor():
    area=None
    if request.method == 'POST':
        area=request.form['area']
        bhk=request.form['bhk']
        print(area+bhk)
        
        # return redirect(url_for('op'))
    return render_template('predict.html',area=area)
     

# @app.route("/op",methods=['GET','POST'])
# def op():
#     if request.method == 'POST':

#     # a=area
#         print(f"area: {area}")
#         return redirect(url_for('price_predictor'))
#     return render_template("predict.html",area=area)




if __name__ == "__main__":
    app.run(debug=True)