from api.message_handler import process_message_with_tensorflow
from config.config import Config

db = Config.get_database()

def save_message(processed_message, chat_id, username, date):
    
    max_prob_class = process_message_with_tensorflow(processed_message)

    user = db.users.find_one({'_id': chat_id})

    if user is None:
        user_data = {
            "_id": chat_id,
            "username": username,
            "threat": 0,
            "insult": 0,
            "obscene": 0,
            "neutral": 0,
            "total_messages": 0,
            "rating": 0.0,
            "messages": []
        }
        user = db.users.insert_one(user_data)
        user = db.users.find_one({'_id': chat_id})

    user[processed_message] += 1
    user['total_messages'] += 1

    attr = {
        "threat": 1,
        "insult": 0.75,
        "obscene": 0.5
    }
    res = 0
    for i in attr:
        res += user[i] * attr[i]
    user['rating'] = res

    user['messages'].append({
        'class': max_prob_class,
        'date': date
    })

    db.users.update_one({'_id': chat_id}, {'$set': user})

