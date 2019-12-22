import vk_api
import random
import time
import json
import sqlite3
import re
import random

conn = sqlite3.connect('kinoteatrupdate.db')
cursor = conn.cursor()

conn1 = sqlite3.connect('irk.db')
cursor1 = conn1.cursor()

conn2 = sqlite3.connect('cinemas.db')
cursor2 = conn2.cursor()


name_kinotheathreskaro = ''
name_kinotheathreskaro_list = []
for i in range(len(cursor2.execute('select name from cinema_halls').fetchall())):
    name_kinotheathreskaro += str(i+1) +'. '+cursor2.execute('select name from cinema_halls').fetchall()[i][0]+'\n'
    name_kinotheathreskaro_list.append(cursor2.execute('select name from cinema_halls').fetchall()[i][0])



date_karo = []
for i in range(8):
    date_karo.append(cursor2.execute('select distinct date from sessions').fetchall()[:8][i][0]+'🤪')


nmt=''
name_theathres_metro = list(set(cursor.execute('select teathres,"Метро:",metro from cinemas').fetchall()))
name_theathres_metro.sort()
for i, e in enumerate(name_theathres_metro):
    name_theathres_metro[i] = re.sub("(\()|(\))|(')|(,)", '', str(name_theathres_metro[i]))
dic_namekinoteatr = {i+1:str(i+1)+'. '+name_theathres_metro[i] for i in range(len(name_theathres_metro))}
dic_namekinoteatr_check = list(dic_namekinoteatr.keys())
for i in range(len(dic_namekinoteatr_check)):
    dic_namekinoteatr_check[i] = str(dic_namekinoteatr_check[i])
check_btn_karo = []
for i in range(172):
    check_btn_karo.append(f'{i+1}😇')



name_theathres = list(set(cursor.execute('select teathres from cinemas').fetchall()))
name_theathres.sort()
for i, e in enumerate(name_theathres):
    name_theathres[i] = re.sub("(\()|(\))|(')|(,)", '', str(name_theathres[i]))


date_irk1 = []
date_irk = cursor1.execute(f'select distinct date from cinemas').fetchall()
for i in date_irk:
     date_irk1.append(re.sub('(\()|(\))|(,)|(\')', '', str(i)))
finders = re.compile('[0123456789]')
for i in range(len(date_irk1)):
    finders = re.search('[0123456789]', date_irk1[i])
    date_irk1[i] = date_irk1[i][int(finders.start()):]
date_irk_dic = {}
for i, e in enumerate(date_irk1):
    date_irk_dic[e] = i


def get_button(label, color, payload=""):
    return {
      "action": {
        "type": "text",
        "payload": json.dumps(payload),
        "label": label
      },
        "color": color
    }
colors = ['primary', 'secondary', 'negative', 'positive']
keyboard = {
    "one_time": True,
    "buttons": [
        [get_button(label='Москва', color=f'{colors[random.randint(0 ,len(colors)-1)]}'),
         get_button(label='Иркутск', color=f'{colors[random.randint(0 ,len(colors)-1)]}')
        ]
    ]
}
formoscow = {
    "one_time": False,
    "buttons": [
        [get_button(label='KARO', color='positive'),
         get_button(label='kinoteatr.ru', color='positive')
        ]
    ]
}
date_kinoteatr = list(set(cursor.execute('select date from cinemas').fetchall()))
date_kinoteatr.sort()
for i, e in enumerate(date_kinoteatr):
    date_kinoteatr[i] = re.sub("(\()|(\))|(')|(,)", '', str(date_kinoteatr[i]))
name_of_kino = {
    "one_time": False,
    "buttons": [
        [get_button(label=f'{1+(i*4)+k}', color=f'{colors[k]}') for k in range(4)
        ]  for i in range(len(name_theathres)//4)
    ]
}
date_kino = {
    "one_time": False,
    "buttons": [
        [get_button(label=f'{date_kinoteatr[i]}', color=f'{colors[random.randint(0 ,len(colors)-1)]}')
        ]  for i in range(len(date_kinoteatr))
    ]
}
irk_kino= {
    "one_time": False,
    "buttons": [
        [get_button(label='Киноквартал', color='primary')
        ]
    ]
}
date_irk_btn= {
    "one_time": False,
    "buttons": [
        [get_button(label=f'{date_irk1[i]}', color='primary') for i in range(4)
        ]
    ]
}

karo_btn = {
    "one_time": False,
    "buttons": [
        [get_button(label=f'{1+(i*4)+k}🧐', color=f'{colors[k]}') for k in range(4)
        ]  for i in range(len(cursor2.execute('select name from cinema_halls').fetchall())//4)
    ]
}
date_karo_btn = {
    "one_time": False,
    "buttons": [
        [get_button(label=f'{date_karo[(i*2)+k]}', color=f'{colors[random.randint(0 ,len(colors)-1)]}') for k in range(2)
        ]  for i in range(len(date_karo)//2)
    ]
}
film_karo_btn = {
    "one_time": False,
    "buttons": [
        [get_button(label=f'{1+(i*4)+k}😇', color=f'{colors[random.randint(0 ,len(colors)-1)]}') for k in range(4)
        ]  for i in range(39//4)
    ]
}
film_karo_btn["buttons"].append([get_button(label='>', color='primary')])
film1_karo_btn = {
    "one_time": False,
    "buttons": [
        [get_button(label=f'{1+(i*4)+k+36}😇', color=f'{colors[random.randint(0 ,len(colors)-1)]}') for k in range(4)
        ]  for i in range(39//4)
    ]
}
film2_karo_btn = {
    "one_time": False,
    "buttons": [
        [get_button(label=f'{1+(i*4)+k+72}😇', color=f'{colors[random.randint(0 ,len(colors)-1)]}') for k in range(4)
        ]  for i in range(39//4)
    ]
}
film3_karo_btn = {
    "one_time": False,
    "buttons": [
        [get_button(label=f'{1+(i*4)+k+108}😇', color=f'{colors[random.randint(0 ,len(colors)-1)]}') for k in range(4)
        ]  for i in range(39//4)
    ]
}
film4_karo_btn = {
    "one_time": False,
    "buttons": [
        [get_button(label=f'{1+(i*4)+k+144}😇', color=f'{colors[random.randint(0 ,len(colors)-1)]}') for k in range(4)
        ]  for i in range(28//4)
    ]
}
film1_karo_btn["buttons"].append([get_button(label='back', color='primary'), get_button(label='forward', color='primary')])
film2_karo_btn["buttons"].append([get_button(label='backward', color='primary'), get_button(label='next', color='primary')])
film3_karo_btn["buttons"].append([get_button(label='назад', color='primary'), get_button(label='вперед', color='primary')])
film4_karo_btn["buttons"].append([get_button(label='⬅', color='primary')])
name_of_kino["buttons"].append([get_button(label='25', color=f'{colors[random.randint(0 ,len(colors)-1)]}')])
keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
keyboard = str(keyboard.decode('utf-8'))
formoscow = json.dumps(formoscow, ensure_ascii=False).encode('utf-8')
formoscow = str(formoscow.decode('utf-8'))
date_kino = json.dumps(date_kino, ensure_ascii=False).encode('utf-8')
date_kino = str(date_kino.decode('utf-8'))
name_of_kino = json.dumps(name_of_kino, ensure_ascii=False).encode('utf-8')
name_of_kino = str(name_of_kino.decode('utf-8'))
irk_kino = json.dumps(irk_kino, ensure_ascii=False).encode('utf-8')
irk_kino = str(irk_kino.decode('utf-8'))
date_irk_btn = json.dumps(date_irk_btn, ensure_ascii=False).encode('utf-8')
date_irk_btn = str(date_irk_btn.decode('utf-8'))
karo_btn = json.dumps(karo_btn, ensure_ascii=False).encode('utf-8')
karo_btn = str(karo_btn.decode('utf-8'))
date_karo_btn = json.dumps(date_karo_btn, ensure_ascii=False).encode('utf-8')
date_karo_btn = str(date_karo_btn.decode('utf-8'))
film_karo_btn = json.dumps(film_karo_btn, ensure_ascii=False).encode('utf-8')
film_karo_btn = str(film_karo_btn.decode('utf-8'))
film1_karo_btn = json.dumps(film1_karo_btn, ensure_ascii=False).encode('utf-8')
film1_karo_btn = str(film1_karo_btn.decode('utf-8'))
film2_karo_btn = json.dumps(film2_karo_btn, ensure_ascii=False).encode('utf-8')
film2_karo_btn = str(film2_karo_btn.decode('utf-8'))
film3_karo_btn = json.dumps(film3_karo_btn, ensure_ascii=False).encode('utf-8')
film3_karo_btn = str(film3_karo_btn.decode('utf-8'))
film4_karo_btn = json.dumps(film4_karo_btn, ensure_ascii=False).encode('utf-8')
film4_karo_btn = str(film4_karo_btn.decode('utf-8'))


ya_ustal_pridumivat = []
for i in range(25):
    ya_ustal_pridumivat.append(f'{i}'+'.')
ya_ustal_pridumivat_irk = []
for i in range(25):
    ya_ustal_pridumivat_irk.append(f'{i+1}'+'.'+' 😋')
ya_ustal_pridumivat_karo = []
for i in range(len(cursor2.execute('select name from cinema_halls').fetchall())):
    ya_ustal_pridumivat_karo.append(f'{i+1}'+'🧐')
films_karo = []
for i in range(len(cursor2.execute('select distinct name from cinemas').fetchall())):
    films_karo.append(cursor2.execute('select distinct name from cinemas').fetchall()[i][0])
btn_films_karo = []
for i in range(len(films_karo)):
    btn_films_karo.append(f'{i+1}'+'😈')


films_karo_str = ''
for i in range(len(films_karo)):
    films_karo_str+= str(i+1)+'. '+films_karo[i]+'\n'



namemsg = ''
for i in range(len(name_theathres)):
    namemsg+='\n'+str(i+1)+'. '+name_theathres[i]

token = "echo "# <Фамилия_группа>" >> README.md "

vk = vk_api.VkApi(token=token)

vk._auth_token()

while True:
    try:
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
        if messages["count"] >= 1:
            id = messages["items"][0]["last_message"]["from_id"]
            body = messages["items"][0]["last_message"]["text"]
            if body.lower() == "начать":
                vk.method("messages.send",
                          {"peer_id": id, "message": "Привет, выбери город, в котором ты бы хотел увидеть сеансы",
                           "random_id": random.randint(1, 2147483647), "keyboard": keyboard})


            elif body.lower() == "москва":
                vk.method("messages.send",
                          {"peer_id": id, "message": "Какой кинотеатр?", "random_id": random.randint(1, 2147483647),
                           "keyboard": formoscow})

            elif body.lower() == "иркутск":
                vk.method("messages.send", {"peer_id": id, "message": "Выберите кинотеатр, в который хотели бы пойти",
                                            "random_id": random.randint(1, 2147483647), "keyboard": irk_kino})

            elif body.lower() == "киноквартал":
                vk.method("messages.send", {"peer_id": id, "message": "Когда вы хотите пойти в кино?",
                                            "random_id": random.randint(1, 2147483647), "keyboard": date_irk_btn})

            elif body.lower() in date_irk1:
                save_date_irk = date_irk_dic[body.lower()]
                pomogite = str(date_irk[save_date_irk])
                pomogite = re.sub('(\()|(\))|(,)|(\')', '', pomogite)
                forsql1 = date_irk[save_date_irk]
                forsql1 = re.sub('(\()|(\))|(,)|(\')', '', str(forsql1))
                forsql1 = cursor1.execute(f'select name from cinemas where date="{forsql1}"').fetchall()
                save_films_irk = []
                for i in range(len(forsql1)):
                    a = re.sub('(\()|(\))|(,)|(\')', '', str(forsql1[i]))
                    save_films_irk.append(f'{i + 1}. {a} \n')
                save_films_irkstr = ''
                for i in save_films_irk:
                    btnfilms_irk = {"one_time": False,
                                    "buttons": [
                                        [get_button(label=f'{1 + (i * 4) + k}. &#128523;', color=f'{colors[k]}') for k
                                         in range(4)
                                         ] for i in range(24 // 4)
                                    ]}
                    btnfilms_irk = json.dumps(btnfilms_irk, ensure_ascii=False).encode('utf-8')
                    btnfilms_irk = str(btnfilms_irk.decode('utf-8'))
                    save_films_irkstr += i
                vk.method("messages.send", {"peer_id": id,
                                            "message": f"Выберите фильм, на который вы желаете пойти\n{save_films_irkstr}",
                                            "random_id": random.randint(1, 2147483647), "keyboard": btnfilms_irk})

            elif body.lower() in ya_ustal_pridumivat_irk:
                try:
                    if len(body.lower()) > 4:
                        qwerty3 = cursor1.execute(
                            f'select session from cinemas where name="{save_films_irk[int(body.lower()[:-3]) - 1][4:-2]}" and date="{pomogite}"').fetchall()
                        qwerty3 = re.sub('(\[)|(\])|(\')|(\")|(2009)|(u)|(\\\\)|(,)|(()|())', '', str(qwerty3))
                    else:
                        qwerty3 = cursor1.execute(
                            f'select session from cinemas where name="{save_films_irk[int(body.lower()[:-3]) - 1][3:-2]}" and date="{pomogite}"').fetchall()
                        qwerty3 = re.sub('(\[)|(\])|(\')|(\")|(2009)|(u)|(\\\\)|(,)|(()|())', '', str(qwerty3))
                    vk.method("messages.send",
                              {"peer_id": id, "message": f"{str(qwerty3)}", "random_id": random.randint(1, 2147483647)})
                    vk.method("messages.send", {"peer_id": id,
                                                "message": "Хочешь посмотреть еще? Выбери город, в котором ты бы хотел увидеть сеансы",
                                                "random_id": random.randint(1, 2147483647), "keyboard": keyboard})
                except:
                    vk.method("messages.send", {"peer_id": id, "message": "на данную кнопку нет фильма",
                                                "random_id": random.randint(1, 2147483647)})








            elif body.lower() == "kinoteatr.ru":
                vk.method("messages.send", {"peer_id": id, "message": f"Какого числа вы хотите пойти в кино?",
                                            "random_id": random.randint(1, 2147483647), "keyboard": date_kino})


            elif body.lower() in date_kinoteatr:
                save_date = body.lower()
                vk.method("messages.send",
                          {"peer_id": id, "message": f"В какой кинотеатр вы бы хотели пойти?\n{namemsg}",
                           "random_id": random.randint(1, 2147483647), "keyboard": name_of_kino})

            elif body.lower() in dic_namekinoteatr_check:
                save_name = name_theathres[int(body.lower()) - 1]
                final_result = ''
                qwerty = cursor.execute(
                    f"select name, genres from cinemas WHERE teathres='{save_name}' AND date='{save_date}'").fetchall()
                for i, e in enumerate(qwerty):
                    for k in range(2):
                        final_result += str(i + 1) + '. ' + qwerty[i][k] + ' '
                    final_result += '\n'
                    btnfilms = {"one_time": False,
                                "buttons": [
                                    [get_button(label=f'{1 + (i * 4) + k}.', color=f'{colors[k]}') for k in range(4)
                                     ] for i in range(24 // 4)
                                ]}
                    btnfilms = json.dumps(btnfilms, ensure_ascii=False).encode('utf-8')
                    btnfilms = str(btnfilms.decode('utf-8'))

                vk.method("messages.send", {"peer_id": id,
                                            "message": f"Выберите фильм, сеансы которого хотите посмотреть:\n{final_result}",
                                            "random_id": random.randint(1, 2147483647), "keyboard": btnfilms})


            elif body.lower() in ya_ustal_pridumivat:
                try:
                    qwerty2 = cursor.execute(
                        f"select name, session from cinemas WHERE teathres='{save_name}' AND date='{save_date}' AND name='{qwerty[int(ya_ustal_pridumivat[int(body.lower()[:-1])][:-1]) - 1][0]}'").fetchall()
                    qwerty2 = qwerty2[0][0] + re.sub("(\()|(\))|(')|(,)", '', str(qwerty2[0][1]))
                    vk.method("messages.send",
                              {"peer_id": id, "message": f"{qwerty2}", "random_id": random.randint(1, 2147483647)})
                    vk.method("messages.send", {"peer_id": id,
                                                "message": "Хочешь посмотреть еще? Выбери город, в котором ты бы хотел увидеть сеансы",
                                                "random_id": random.randint(1, 2147483647), "keyboard": keyboard})
                except:
                    vk.method("messages.send", {"peer_id": id, "message": "на данную кнопку нет фильма",
                                                "random_id": random.randint(1, 2147483647)})

            elif body.lower() == 'karo':
                vk.method("messages.send", {"peer_id": id,
                                            "message": f"Выберите кинотеатр, в который бы хотели пойти:\n{name_kinotheathreskaro}",
                                            "random_id": random.randint(1, 2147483647), "keyboard": karo_btn})

            elif body.lower() in ya_ustal_pridumivat_karo:
                save_id_theathres = cursor2.execute(
                    f'select id from cinema_halls where name="{name_kinotheathreskaro_list[int(body.lower()[:-1]) - 1]}"').fetchall()[
                    0][0]
                vk.method("messages.send", {"peer_id": id, "message": f"Выберите, какого числа вы бы хотели пойти:",
                                            "random_id": random.randint(1, 2147483647), "keyboard": date_karo_btn})


            elif body.lower() in date_karo:
                save_date_karo = body.lower()[:-1]
                vk.method("messages.send",
                          {"peer_id": id, "message": f"Укажите, на какой фильм вы бы хотели пойти:\n{films_karo_str}",
                           "random_id": random.randint(1, 2147483647), "keyboard": film_karo_btn})
            elif body.lower() == '>':
                vk.method("messages.send",
                          {"peer_id": id, "message": f"Укажите, на какой фильм вы бы хотели пойти:\n{films_karo_str}",
                           "random_id": random.randint(1, 2147483647), "keyboard": film1_karo_btn})
            elif body.lower() == 'back':
                vk.method("messages.send",
                          {"peer_id": id, "message": f"Укажите, на какой фильм вы бы хотели пойти:\n{films_karo_str}",
                           "random_id": random.randint(1, 2147483647), "keyboard": film_karo_btn})
            elif body.lower() == 'forward':
                vk.method("messages.send",
                          {"peer_id": id, "message": f"Укажите, на какой фильм вы бы хотели пойти:\n{films_karo_str}",
                           "random_id": random.randint(1, 2147483647), "keyboard": film2_karo_btn})
            elif body.lower() == 'backward':
                vk.method("messages.send",
                          {"peer_id": id, "message": f"Укажите, на какой фильм вы бы хотели пойти:\n{films_karo_str}",
                           "random_id": random.randint(1, 2147483647), "keyboard": film1_karo_btn})
            elif body.lower() == 'next':
                vk.method("messages.send",
                          {"peer_id": id, "message": f"Укажите, на какой фильм вы бы хотели пойти:\n{films_karo_str}",
                           "random_id": random.randint(1, 2147483647), "keyboard": film3_karo_btn})
            elif body.lower() == 'назад':
                vk.method("messages.send",
                          {"peer_id": id, "message": f"Укажите, на какой фильм вы бы хотели пойти:\n{films_karo_str}",
                           "random_id": random.randint(1, 2147483647), "keyboard": film2_karo_btn})
            elif body.lower() == 'вперед':
                vk.method("messages.send",
                          {"peer_id": id, "message": f"Укажите, на какой фильм вы бы хотели пойти:\n{films_karo_str}",
                           "random_id": random.randint(1, 2147483647), "keyboard": film4_karo_btn})
            elif body.lower() == '⬅':
                vk.method("messages.send",
                          {"peer_id": id, "message": f"Укажите, на какой фильм вы бы хотели пойти:\n{films_karo_str}",
                           "random_id": random.randint(1, 2147483647), "keyboard": film3_karo_btn})

            elif body.lower() in check_btn_karo:
                final_result_karo = ''
                try:
                    save_namefilm_karo = films_karo[int(body.lower()[:-1]) - 1]
                    save_idfilm_karo = \
                    cursor2.execute(f"select id from cinemas WHERE name='{save_namefilm_karo}'").fetchall()[0][0]
                    final_result_karo = cursor2.execute(
                        f"select time,date,price from sessions WHERE date='{save_date_karo}' AND hall_id='{save_id_theathres}' AND cinema_id='{save_idfilm_karo}'").fetchall()
                    vse = f'Название фильма: {save_namefilm_karo}' + f'\nВремя сеанса: {final_result_karo[0][0]}' + f'\nДата: {final_result_karo[0][1]}' + f'\nЦена: {final_result_karo[0][2]}'
                    vk.method("messages.send",
                              {"peer_id": id, "message": f"{vse}", "random_id": random.randint(1, 2147483647)})
                except:
                    vk.method("messages.send",
                              {"peer_id": id, "message": f"на {save_date_karo} данного фильма нет в прокате",
                               "random_id": random.randint(1, 2147483647)})








            else:
                vk.method("messages.send", {"peer_id": id, "message": "я не знаю что значит " + str(body.lower()),
                                            "random_id": random.randint(1, 2147483647)})
    except Exception as E:
        time.sleep(1)


