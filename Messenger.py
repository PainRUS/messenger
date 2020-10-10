def send_message(text, author):
    if isinstance(text, str) and isinstance(author, str):

        """todo: сохранить в БД"""
        print(text, author)
        return  "OK"
    else:
        return "Not OK"


result = send_message("Привет", "Иван")
print(result)
result = send_message("Здравствуйте", "Василий")
print(result)
result = send_message(2, "Иван")
print(result)

#class Messenger:
    # db
    # send_message
    # ...
    