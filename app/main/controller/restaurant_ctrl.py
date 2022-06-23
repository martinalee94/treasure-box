from flask_restx import Resource 

from app.main.dto import restaurant as restaurant_dto_file

api = restaurant_dto_file.api
RestaurantDto = restaurant_dto_file.RestaurantDto
parser = api.parser()

@api.route('/')
class RestaurantAPI(Resource):
    @api.response(200, 'Success', RestaurantDto.restaurant_list_resp_model)
    @api.response(400, 'Fail')
    def get(self):
        
        return