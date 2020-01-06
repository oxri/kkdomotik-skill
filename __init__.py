from mycroft import MycroftSkill, intent_file_handler


class Kkdomotik(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('kkdomotik.intent')
    def handle_kkdomotik(self, message):
        self.speak_dialog('kkdomotik')


def create_skill():
    return Kkdomotik()

