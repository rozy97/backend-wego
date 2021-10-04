from datetime import datetime

def check_date(date_string):
    format = '%Y-%m-%d'
    try:
        datetime.strptime(date_string, format)
        return True
    except ValueError:
        return False

def check_gender(gender):
    genders = ["man", "woman"]
    gender = gender.lower()
    if gender in genders:
        return True
    else:
        return False

def check_user_id(id):
    return id.isnumeric()
