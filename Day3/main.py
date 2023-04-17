class Situation:
    def __init__(self, desc, acts):
        self.desc = desc
        self.acts = acts
    def description(self):
        return self.desc + " Wähle eine der folgenden Aktionen: " + str(self.acts.keys())
    def actions(self):
        return self.acts
    def choose_action(self, action):
        return self.acts.get(action)

Ertrunken = Situation("Du bist ertrunken", {})
Schatz = Situation("Du hast den Schatz gefunden", {})
Am_See = Situation("Am See", {"Schwimme":Ertrunken, "Boot":Schatz})
print(Am_See.description())


current_situation = Am_See
fertig = False

while not fertig:
    print(current_situation.description())
    action = input("choose an action: ")
    current_situation = current_situation.choose_action(action)






