import re

def remove_links(text):
    # Удаляем ссылки
    text = re.sub(r'http\S+|www\S+|https\S+', '', text)
    return text

def remove_extra_spaces(text):
    # Удаляем лишние пробелы
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def remove_emojis(text):
    # Удаляем смайлики и эмодзи
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # Смайлики
                               u"\U0001F300-\U0001F5FF"  # Символы и пиктограммы
                               u"\U0001F680-\U0001F6FF"  # Транспорт и символы
                               u"\U0001F1E0-\U0001F1FF"  # Флаги стран
                               u"\U00002702-\U000027B0"  # Дополнительные символы
                               u"\U000024C2-\U0001F251" 
                               "]+", flags=re.UNICODE)
    text = emoji_pattern.sub(r'', text)
    return text

def preprocess_text(text):
    # Удаление ссылок
    text = remove_links(text)
    # Удаление лишних пробелов
    text = remove_extra_spaces(text)
    # Удаление смайликов
    text = remove_emojis(text)
    return text

# Пример использования
text = "Привет! Это ссылка на сайт: https://example.com.    Текст с    лишними пробелами. 😃"
processed_text = preprocess_text(text)
print(processed_text)
