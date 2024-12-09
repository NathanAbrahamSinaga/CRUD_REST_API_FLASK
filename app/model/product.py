from app import db
class Product(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(230), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def __repr__(self):
        return '<Product %r>' % self.name
