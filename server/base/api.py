from flask import request, jsonify, Blueprint


from db.models import Prediction
from ml_model.model_base import get_prediction


api = Blueprint('api', __name__)


@api.route('/predict', methods=['POST'])
def predict():
    file = request.files['file']
    img_bytes = file.read()
    _, class_name = get_prediction(image_bytes=img_bytes)
    pred = Prediction(file_name=file.filename, predicted_class=class_name)
    return jsonify({"Prediction": str(pred)})




