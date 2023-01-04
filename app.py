from flask import Flask, request, render_template, redirect, url_for
import numpy as np
import pickle
app = Flask(__name__,template_folder='templates')
model=pickle.load(open("model.pkl","rb"))
#  SQL CREDENTIALS
     

## SQL INTEGRATION


## PREDICTION FUNCTION
@app.route("/",methods=['GET','POST'])
def price_predictor():
    if request.method == 'POST':
        int_features=[int(x) for x in request.form.values()]
        final_features=[np.array(int_features)]
        price=model.predict(final_features)[0][0]
        final_price=np.round(price,2)
        print(f"Final features:{final_features}")
        return render_template('predict.html',final_price=final_price)
    return render_template('predict.html')

if __name__ == "__main__":
    app.run(debug=True)