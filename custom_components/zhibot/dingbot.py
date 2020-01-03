
#
from .zhibot import zhibotQuery
from .chatbot import chatbotView

# Logging
import logging
_LOGGER = logging.getLogger(__name__)


#
class dingbotView(chatbotView):

    def check(self, hass, data):
        if data['chatbotUserId'] in self.conf:
            return True
        return super().check(hass, data)

    def config_done(self, data):
        self.conf.append(data['chatbotUserId'])

    def config_desc(self, data):
        return "钉钉群“%s”的“%s”正在试图访问“%s”。\n\nchatbotUserId: %s" % (data['conversationTitle'], data['senderNick'], data['text']['content'], data['chatbotUserId'])

    async def handle(self, hass, data):
        return await zhibotQuery(hass, data['text']['content'])

    def response(self, answer):
        return {'msgtype': 'text', 'text': {'content': answer}}
