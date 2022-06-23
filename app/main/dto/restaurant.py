from doctest import Example
from flask_restx import Namespace
from flask_restx.fields import *

api = Namespace('restaurant', description="식당")

class RestaurantDto:
    restaurant_list_resp_model = api.model('식당 리스트 응답 모델',{
        'id' : String(description = "식당 번호", example = "1"),
        'name' : String(description = "식당 이름", example = "소풍 가는 날"),
        'address' : String(description = "식당 주소", example = "서울특별시 서초구 매헌로 24"),
        'create_date' : String(description = "식당 데이터 등록 일자", example = "2021-07-13 00:00:01")
    })