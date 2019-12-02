import os

from . import webex


def all_spaces():
    res = []
    rooms = webex.rooms.list(teamId=os.environ.get('TEAM_ID'))
    for room in rooms:
        res.append((room.id, room.title))
    return res


def send_message(message, files, spaces):
    for space in spaces:
        print(space)
        if len(files) == 1:
            webex.messages.create(roomId=space, text=message, files=files)
        else:
            webex.messages.create(roomId=space, text=message)
            for file in files:
                webex.messages.create(roomId=space, files=[file])
