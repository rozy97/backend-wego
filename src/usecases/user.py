from ..models import user, last_id
from ..helpers import validator

def get_user_by_id(user_id):
    code = 200

    valid_id = validator.check_user_id(user_id)
    if not valid_id:
        code = 422
        data = {
            'message': 'user id invalid'
        }
        return {
            'code': code,
            'data': data
        }

    data = user.find_by_id(int(user_id))

    if not data:
        code = 404
        data = {
            'message': 'user not found'
        }

    response = {
        'code': code,
        'data': data
    }

    return response

def create_user(new_data):
    code = 200

    dob_valid = validator.check_date(new_data['dob'])
    if not dob_valid:
        code = 422
        data = {
            'message': 'dob invalid'
        }
        return {
            'code': code,
            'data': data
        }

    gender_valid = validator.check_gender(new_data['gender'])
    if not gender_valid:
        code = 422
        data = {
            'message': 'gender invalid'
        }
        return {
            'code': code,
            'data': data
        }


    new_data['id'] = last_id.generate_id()
    data = user.create(new_data)

    response = {
        'code': code,
        'data': data
    }

    return response
