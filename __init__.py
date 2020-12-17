from mycroft import MycroftSkill, intent_file_handler


class ConsentOverview(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('overview.consent.intent')
    def handle_overview_consent(self, message):
        self.speak_dialog('overview.consent')


def create_skill():
    return ConsentOverview()

