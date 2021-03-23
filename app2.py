from flask import Flask, request, Response
from botbuilder.schema import Activity
from botbuilder.core import BotFrameworkAdapter, BotFrameworkAdapterSettings
import asyncio
 
## for those who are using vscode/ pycharm 
from botstart import bot
###from pythonbotprogram import bot
### end ......
app = Flask(__name__)
loop = asyncio.get_event_loop()
 
botadaptersettings = BotFrameworkAdapterSettings("","")
botadapter = BotFrameworkAdapter(botadaptersettings)
 
### crestin of instance for the class create above 
ebot = bot()
## route for the bot 
@app.route("/api/messages",methods=["POST"])
def messages():
    if "application/json" in request.headers["content-type"]:
        jsonmessage = request.json
    else:
        return Response(status=415)
 
    activity = Activity().deserialize(jsonmessage)
 
    async def turn_call(turn_context):
        await ebot.on_turn(turn_context)
 
    task = loop.create_task(botadapter.process_activity(activity,"",turn_call))
    loop.run_until_complete(task)
 
if __name__ == '__main__':
    app.run('localhost',3978)