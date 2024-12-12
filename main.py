from flask import Flask, request, jsonify
import joblib
import numpy as np

# load the model
model_rf = joblib.load('./models/random_forest_model.pkl')

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json(force=True)
        features = np.array(data['features']).reshape(1, -1)
        prediction = model_rf.predict(features)
        return jsonify({'prediction': prediction[0]})
    except Exception as e:
        return jsonify({'error', str(e)})
    

if __name__ == '__main__':
    app.run(debug=True)