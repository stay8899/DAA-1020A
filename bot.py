#pip install botbuilder-core
#pip install botbuilder-schema

from botbuilder.core import TurnContext
class bot:
    async def turn_on(self, turn_context:TurnContext):
        await turn_context.send_activity(turn_context, activity.text)