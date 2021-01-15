from datetime import datetime as dt
from base import db


class Prediction(db.Model):
    __tablename__ = "predictions"

    id = db.Column(db.Integer, primary_key=True)
    file_name = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=dt.utcnow)
    predicted_class = db.Column(db.String, nullable=False)

    def __repr__(self):
        return 'Prediction<{0}, {1}, {2}>'.format(self.file_name, self.created_at, self.predicted_class)
