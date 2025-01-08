from marshmallow import Schema, fields

class RoleSchema(Schema):
    id = fields.Integer(required=False)  
    role_name = fields.String(required=True)  

    class Meta:
        fields = ('id', 'role_name')  

# Single and multiple schemas
role_schema = RoleSchema()
roles_schema = RoleSchema(many=True)