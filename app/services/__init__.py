import os

from webexteamssdk import WebexTeamsAPI

webex = WebexTeamsAPI(os.environ.get('BOT_TOKEN'))
web_hooks = webex.webhooks.list()
for web_hook in web_hooks:
    webex.webhooks.delete(web_hook.id)
webex.webhooks.create(name='Developmnet', targetUrl=os.environ.get('BOT_URL'), resource='messages', event='created')
