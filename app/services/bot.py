import os

from webexteamssdk import ApiError

from . import webex


def all_spaces():
    res = []
    try:
        rooms = webex.rooms.list(teamId=os.environ.get('TEAM_ID'))
        for room in rooms:
            res.append((room.id, room.title))
        res.append(('Y2lzY29zcGFyazovL3VzL1JPT00vYjI3Y2VkNjAtODY0My0xMWU0LTlhN2UtNjM4ODY3OGNmNmZh', 'Swiss Collab Partner Community'))
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
