import telebot
from config import *
from zabbix import Zabbix

bot = telebot.TeleBot(TOKEN_TELEGRAM)
zaip = Zabbix()
# {'content_type': 'text', 'id': 772, 'message_id': 772, 'from_user': {'id': 685334242, 'is_bot': False, 'first_name': 'Jeyson', 'username': 'JeysonHilario', 'last_name': 'Hilario', 'language_code': 'pt-br', 'can_join_groups': None, 'can_read_all_group_messages': None, 'supports_inline_queries': None, 'is_premium': None, 'added_to_attachment_menu': None}, 'date': 1662032029, 'chat': {'id': 685334242, 'type': 'private', 'title': None, 'username': 'JeysonHilario', 'first_name': 'Jeyson', 'last_name': 'Hilario', 'photo': None, 'bio': None, 'join_to_send_messages': None, 'join_by_request': None, 'has_private_forwards': None, 'has_restricted_voice_and_video_messages': None, 'description': None, 'invite_link': None, 'pinned_message': None, 'permissions': None, 'slow_mode_delay': None, 'message_auto_delete_time': None, 'has_protected_content': None, 'sticker_set_name': None, 'can_set_sticker_set': None, 'linked_chat_id': None, 'location': None}, 'sender_chat': None, 'forward_from': None, 'forward_from_chat': None, 'forward_from_message_id': None, 'forward_signature': None, 'forward_sender_name': None, 'forward_date': None, 'is_automatic_forward': None, 'reply_to_message': None, 'via_bot': None, 'edit_date': None, 'has_protected_content': None, 'media_group_id': None, 'author_signature': None, 'text': '/host', 'entities': [<telebot.types.MessageEntity object at 0x00000273A7D939A0>], 'caption_entities': None, 'audio': None, 'document': None, 'photo': None, 'sticker': None, 'video': None, 'video_note': None, 'voice': None, 'caption': None, 'contact': None, 'location': None, 'venue': None, 'animation': None, 'dice': None, 'new_chat_member': None, 'new_chat_members': None, 'left_chat_member': None, 'new_chat_title': None, 'new_chat_photo': None, 'delete_chat_photo': None, 'group_chat_created': None, 'supergroup_chat_created': None, 'channel_chat_created': None, 'migrate_to_chat_id': None, 'migrate_from_chat_id': None, 'pinned_message': None, 'invoice': None, 'successful_payment': None, 'connected_website': None, 'reply_markup': None, 'json': {'message_id': 772, 'from': {'id': 685334242, 'is_bot': False, 'first_name': 'Jeyson', 'last_name': 'Hilario', 'username': 'JeysonHilario', 'language_code': 'pt-br'}, 'chat': {'id': 685334242, 'first_name': 'Jeyson', 'last_name': 'Hilario', 'username': 'JeysonHilario', 'type': 'private'}, 'date': 1662032029, 'text': '/host', 'entities': [{'offset': 0, 'length': 5, 'type': 'bot_command'}]}}

@bot.message_handler(commands=["enviarhostsup"])
def SendHostUp(response):
    chatid = response.chat.id
    bot.send_message(chatid,"Processando Dados Aguarde !!!")
    dados = zaip.item_get_hosts_up()
    for i in dados:
        try:
            bot.send_message(chatid,f"HOST: {i[0]}\n"
                                    f"SSID: {i[1]}\n"
                                    f"Frequencia: {i[2]}\n"
                                    f"IP: {i[3]}\n"
                                    f"Estacoes Conectadas: {i[4]}\n"
                             )
        except IndexError:
            pass

@bot.message_handler(commands=["enviarhostsdown"])
def SendHostDown(response):
    chatid = response.chat.id
    dados = zaip.item_get_hosts_down()

    if dados == []:
        bot.send_message(chatid,"Nao existe nenhum host off no momento")
        return

    for i in dados:
        try:
            bot.send_message(chatid,f"HOST: {i[0]}\n"
                                    f"SSID: {i[1]}\n"
                                    f"Frequencia: {i[2]}\n"
                                    f"IP: {i[3]}\n"
                                    f"Estacoes Conectadas: {i[4]}\n"
                             )
        except IndexError:
            bot.send_message(chatid,f"Esse Host Nao Possui essas Informações {i}")
            pass

def verificar(response):
        return True

@bot.message_handler(func=verificar)
def messageFirst(response):
    bot.reply_to(response,
                 f"Olá o que Voce Deseja ?\n"
                 f"/enviarhostsup - Retornar dados dos Dispositivos OFF\n"
                 f"/enviarhostsdown - Retornar dados dos Dispositivos ON\n"
                 f"/TESTE - TESTE * "

                 )

def runBot():
    bot.polling()

def stopBot():
    bot.stop_bot()

