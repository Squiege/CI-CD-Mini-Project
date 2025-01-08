from marshmallow import fields
from schema import ma

class CustomerAccountSchema(ma.Schema):
    id = fields.Integer(required=False)
    customer_id = fields.Integer(required=True)
    customer_name = fields.String(required=True)

    class Meta:
        fields = ('id', 'customer_id', 'customer_name')

customer_account_schema = CustomerAccountSchema()
customer_accounts_schema = CustomerAccountSchema(many=True)
