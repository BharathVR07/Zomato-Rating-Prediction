from flask import Flask, render_template, request
import numpy as np
import pickle
import sklearn
from sklearn.preprocessing import StandardScaler


app = Flask(__name__, template_folder='template')

model = pickle.load(open('random_forest_regression_model.pkl','rb'))

@app.route('/', methods = ['GET'])

def Home():
    return render_template('index.html')

@app.route('/predict', methods = ['POST'])
def predict():
    if request.method=='POST':
        rating_text = request.form['rating_text']
        mapped = {'Excellent':1,'Very Good':2,'Good':3,'Average':4,'Poor':5,'Not rated':6}
        if rating_text in mapped:
            rating_text = mapped[rating_text]
        else:
            rating_text = 0

        rating_color = request.form['rating_color']
        mapped = {'Dark Green': 1, 'Green': 2, 'Yellow': 3, 'Orange': 4, 'Red': 5, 'White': 6}
        if rating_color in mapped:
            rating_color=mapped[rating_color]
        else:
            rating_color=0

        votes = request.form['votes']

        average_cost_for_two = request.form['average_cost_for_two']

        price_range = request.form['price_range']

        has_online_delivery = request.form['has_online_delivery']
        if has_online_delivery == 'Yes':
            has_online_delivery=1
        else:
            has_online_delivery=0

        has_table_booking=request.form['has_table_booking']
        if has_table_booking=='Yes':
            has_table_booking=1
        else:
            has_table_booking=0

        locality = request.form['locality']
        if locality=='pitampura':
            locality=1
        else:
            locality=0

        city = request.form['city']
        if city=='new delhi':
            new_delhi=1
            gurgaon=0
            noida=0
        elif city=='gurgaon':
            new_delhi = 0
            gurgaon = 1
            noida = 0
        elif city=='noida':
            new_delhi=0
            gurgaon=0
            noida=1
        else:
            new_delhi = 0
            gurgaon = 0
            noida = 0

        cuisines = request.form['cuisines']
        if cuisines == 'north indian':
            north_indian=1
            north_indian_chinese=0
            north_indian_mughlai=0
            north_indian_mughlai_chinese=0
            chinese=0
            fast_food=0
            cafe=0
            bakery=0
            bakery_desserts=0
        elif cuisines == 'north indian chinese':
            north_indian=0
            north_indian_chinese=1
            north_indian_mughlai=0
            north_indian_mughlai_chinese=0
            chinese=0
            fast_food=0
            cafe=0
            bakery=0
            bakery_desserts=0
        elif cuisines == 'north indian mughlai':
            north_indian=0
            north_indian_chinese=0
            north_indian_mughlai=1
            north_indian_mughlai_chinese=0
            chinese=0
            fast_food=0
            cafe=0
            bakery=0
            bakery_desserts=0
        elif cuisines == 'north indian mughlai chinese':
            north_indian=0
            north_indian_chinese=0
            north_indian_mughlai=0
            north_indian_mughlai_chinese=1
            chinese=0
            fast_food=0
            cafe=0
            bakery=0
            bakery_desserts=0
        elif cuisines == 'chinese':
            north_indian=0
            north_indian_chinese=0
            north_indian_mughlai=0
            north_indian_mughlai_chinese=0
            chinese=1
            fast_food=0
            cafe=0
            bakery=0
            bakery_desserts=0
        elif cuisines == 'fast food':
            north_indian=0
            north_indian_chinese=0
            north_indian_mughlai=0
            north_indian_mughlai_chinese=0
            chinese=0
            fast_food=1
            cafe=0
            bakery=0
            bakery_desserts=0
        elif cuisines == 'cafe':
            north_indian=0
            north_indian_chinese=0
            north_indian_mughlai=0
            north_indian_mughlai_chinese=0
            chinese=0
            fast_food=0
            cafe=1
            bakery=0
            bakery_desserts=0
        elif cuisines == 'bakery':
            north_indian=0
            north_indian_chinese=0
            north_indian_mughlai=0
            north_indian_mughlai_chinese=0
            chinese=0
            fast_food=0
            cafe=0
            bakery=1
            bakery_desserts=0
        elif cuisines == 'bakery_desserts':
            north_indian=0
            north_indian_chinese=0
            north_indian_mughlai=0
            north_indian_mughlai_chinese=0
            chinese=0
            fast_food=0
            cafe=0
            bakery=0
            bakery_desserts=1
        else:
            north_indian=0
            north_indian_chinese=0
            north_indian_mughlai=0
            north_indian_mughlai_chinese=0
            chinese=0
            fast_food=0
            cafe=0
            bakery=0
            bakery_desserts=0

        prediction = model.predict([[rating_text,rating_color,votes,average_cost_for_two,price_range,
                                 has_online_delivery,has_table_booking,locality,new_delhi,gurgaon,noida,
                                north_indian,north_indian_chinese,north_indian_mughlai,
                                 north_indian_mughlai_chinese,chinese,fast_food,cafe,bakery,bakery_desserts]])
        output = round(prediction[0],2)
        return render_template('result.html', prediction_texts='Rating for the restaurant is {:.1f}'.format(output))
    else:
        return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)