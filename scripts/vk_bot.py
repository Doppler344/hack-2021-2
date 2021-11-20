import vk_api


class Bot:
    def __init__(self, token=""):
        self._session = vk_api.VkApi(token=token)

    def send_message(self, destination, message):
        self._session.method("messages.send", {
            "user_id": destination,
            "message": message,
            "random_id": 0
    })



