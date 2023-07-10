from engine.llm.narrator import _Narrator


class CrimeGame:
    def __init__(self):
        self.history = []
        self.current_scene = {"text": "", "image": ""}
        self.available_actions = []
        self.taken_actions = 0
        self.total_actions = 25
        self.narrator = _Narrator()

    async def take_option(self, option):
        action = option

        self.history.append(
            {
                "text": self.current_scene["text"],
                "action": action,
                "image": self.current_scene["image"],
            }
        )
        self.taken_actions += 1
        history = "\n".join([entry["text"] for entry in self.history])
        self.current_scene = await self.narrator.next_scene(
            history=history, last_action=action
        )

        return {
            "display": {
                "action": action,
                "text": self.current_scene["text"],
                "image": self.current_scene["image_url"],
                "taken_actions": self.taken_actions,
                "total_actions": self.total_actions,
                "available_actions": self.current_scene["available_actions"],
            }
        }

    def intro(self):
        return "*🔍 Welcome to the world of GPT-powered investigations. Prepare for an exciting conversational adventure in crime-solving! 🕵️‍♂️*"

    async def new_story(self):
        self.current_scene = await self.narrator.new_story()
        self.taken_actions += 1

        return {
            "display": {
                "action": None,
                "text": self.current_scene["text"],
                "image": self.current_scene["image_url"],
                "taken_actions": self.taken_actions,
                "total_actions": self.total_actions,
                "available_actions": self.current_scene["available_actions"],
            }
        }

    def restart(self):
        self.history = []
        self.current_scene = {"text": "", "image": ""}
        self.available_actions = []
        self.taken_actions = 0
