import numpy as np
from flask import Flask, abort, jsonify, request
import pickle
import numpy as np
import sys


#asset_ret_model = pickle.load(open("asset_ret_model.pkl", "rb"))

app = Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def index():
#    result = 10/0
    return 'hello_world12'

@app.route('/api',methods=['GET', 'POST'])
def make_predict():

    #all kind of error checking should go here
 #   data = request.get_json(force=True)

#    print('Hello world!', file=sys.stderr)


    #convert json to numpy array
   # predict_request = [data['max_inactive_days'],data['neg_trans'],data['pos_trans'],data['aum_change_pct'],data['gross_amt_change']]
  #  predict_request = np.array([predict_request])
   
    #np.array goes into the model and prediction comes out
    #y_pred_value = asset_ret_model.predict(predict_request)
#    y_pred_value = request.args.get('y_pred_value', default = 9, type = int)

    #return our prediction
#    y_pred_value[0] = 1
    #output = int(y_pred_value[0])
    
#    output = [predict_request[0][0]]
#    output = [predict_request]
#    return output
    #return jsonify(results=output)
    return str('vishal chak')
     
if __name__ == '__main__':
    app.run(port=5001, debug=True)
