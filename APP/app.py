from flask import Flask, render_template, request, jsonify
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import joblib

app = Flask(__name__)

# Загрузка модели
model1 = joblib.load('models/catboost_model_1.pkl')
model2 = joblib.load('models/catboost_model_2.pkl')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Получение данных из формы
        data = request.get_json()

        features = [
            float(data['matrix']),
            float(data['density']),
            float(data['density_mod']),
            float(data['hardener_q']),
            float(data['epoxy_groups']),
            float(data['temp']),
            float(data['surface_density']),
            float(data['resin_cons']),
            float(data['angle']),
            float(data['pitch']),
            float(data['patch_density'])
        ]
        # Преобразование в numpy array
        input_features = np.array([features])

        # Масштабирование и предсказание
        strength = model1.predict(input_features)
        elaticity = model2.predict(input_features)

        # Форматирование результата
        result = {
            'elastic_modulus': round(float(strength), 2),
            'tensile_strength': round(float(elaticity), 2),
            'status': 'success'
        }

        return jsonify(result)

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
