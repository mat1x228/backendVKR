import requests
from config.config import Config

db = Config.get_database()
def process_message_with_tensorflow(message):
  
    payload = {
        'instances': [message]
    }

    response = requests.post('http://localhost:8501/v1/models/my_model:predict', json=payload)

    if response.status_code == 200:
        result = response.json()
 
        predictions = result['predictions'][0]

        max_prob_class = max(predictions, key=predictions.get)

    
        return max_prob_class

    else:
        
        return 'Error: Failed to process message'

