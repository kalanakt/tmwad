import requests

class closeGeneralForumTopic:
    def __init__(self, token):
        self.token = token
        self.base_url = f'https://api.telegram.org/bot{token}'

    def close_general_forum_topic(self, chat_id):
        url = f'{self.base_url}/closeGeneralForumTopic'
        data = {'chat_id': chat_id}
        response = requests.post(url, json=data)
        return response.json()
