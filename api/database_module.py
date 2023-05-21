from config.config import Config

db = Config.get_database()

def get_users():
    users = db.users.find()
    user_list = [{'_id': user['_id'], 'username': user['username'], 'rating': user['rating']} for user in users]
    sorted_users = sorted(user_list, key=lambda user: user['rating'], reverse=True)
    return sorted_users

def get_user_by_id(user_id):
    user = db.users.find_one({'_id': user_id})
    return user
