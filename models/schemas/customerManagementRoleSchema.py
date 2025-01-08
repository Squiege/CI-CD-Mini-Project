from schema import ma
from marshmallow import fields

class CustomerManagementRoleSchema(ma.Schema):
    id = fields.Integer(required=False)  
    customer_id = fields.Integer(required=True)  
    role_id = fields.Integer(required=True)  

    class Meta:
        fields = ('id', 'customer_id', 'role_id') 

customer_management_role_schema = CustomerManagementRoleSchema()
customer_management_roles_schema = CustomerManagementRoleSchema(many=True)
