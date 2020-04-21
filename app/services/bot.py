import os

from webexteamssdk import ApiError, Webhook

from . import webex


def all_spaces():
    res = []
    try:
        memberships = webex.memberships.list()
        for membership in memberships:
            room = webex.rooms.get(roomId=membership.roomId)
            if(room.teamId):
                team = webex.teams.get(teamId=room.teamId)
                res.append((room.id, team.name + ' - ' +  room.title))
            else:
                res.append((room.id, room.title))
        return res
    except ApiError as e:
        return res


def send_message(message, files, spaces):
    response = []
    for space in spaces:
        try:
            if len(files) == 1:
                webex.messages.create(roomId=space, text=message, files=files)
            else:
                webex.messages.create(roomId=space, text=message)
                for file in files:
                    webex.messages.create(roomId=space, files=[file])
        except ApiError as e:
            room = webex.rooms.get(roomId=space)
            response.append(room.title)
            pass
    return response

def is_authorized(webhook_obj):
    message = webex.messages.get(webhook_obj.data.id)
    if(message.personId in os.environ.get('ADMIN').split(',')):
        return True
    else:
        return False

def get_email(webhook_obj):
    message = webex.messages.get(webhook_obj.data.id)
    person = webex.people.get(personId=message.personId)
    if person:
        return person.emails[0]

def send_login_link(webhook_obj, token):
    message = webex.messages.get(webhook_obj.data.id)
    webex.messages.create(toPersonId=message.personId, text="Hey, please find your login link here: \n" + os.environ.get('MAIN_URL') +  "login?token="+token)
    return

def send_error_message(webhook_obj):
    message = webex.messages.get(webhook_obj.data.id)
    webex.messages.create(toPersonId=message.personId, text='It looks like you are not allowed to request access to this resource!')
    return

def is_me(webhook_obj):
    message = webex.messages.get(webhook_obj.data.id)
    me = webex.people.me()
    if(message.personId == me.id):
        return True
    else:
        return False