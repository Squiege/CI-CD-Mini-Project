from marshmallow import fields
from schema import ma

class CustomerSchema(ma.Schema):
    id = fields.Integer(required=False)
    name = fields.String(required=True)
    email = fields.String(required=True)

    class Meta:
        fields = ('id', 'name', 'email')

customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)