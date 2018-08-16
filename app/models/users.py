from app.models import db
from app.models import ma


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def __serialize__(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email
        }

db.create_all()


class UserSchema(ma.Schema):
    class Meta:
        model = User
        fields = ['id', 'name', 'email']

user_schema = UserSchema(many=True)