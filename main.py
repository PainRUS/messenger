import time

class Messenger:
    def __init__(self):
        self.db = [
            {"text": "Привет", "author": "jack", "time": time.time()},
            {"text": "Привет!", "author": "mary", "time": time.time()},
        ]

    def send_message(self, text, author):
        if isinstance(text, str) and isinstance(author, str):
            self.db.append({
                "text": text,
                "author": author,
                "time": time.time()
            })
            print(text, author)
            return "OK"
        else:
            return "Not OK"

    def get_messages(self):
        return self.db

