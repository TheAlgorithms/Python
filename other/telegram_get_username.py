import telebot

def get_username(chat_id, user_id):
    userinfo_dict = bot.get_chat_member(chat_id, user_id)
    userinfo = userinfo_dict.user
    userinfo = (str(userinfo))
    userinfo = userinfo.replace("'", "\"")
    userinfo = userinfo.replace(": ", ": \"")
    userinfo = userinfo.replace(",", "\",")
    userinfo = userinfo.replace("}", "\"}")
    userinfo = userinfo.replace("\"\"", "\"")
    user_dict = json.loads(userinfo)
    if user_dict['username'] == None:
        usern = user_dict['first_name']
    else:
        usern = user_dict['username']
    return usern
  
print(get_username(1 ,1 ))
