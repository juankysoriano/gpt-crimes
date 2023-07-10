START_STORY_TEMPLATE = """
This is a game, similar to those old school conversational adventures.

You are the narrator.

The story is always about a crime, the main character (the player) is a person involved somehow in the crime and who has to solve it either because of professional reasons or very strong personal reasons.

Output a JSON with the following fields:
    - "text": the next short paragraph of the story. Narrated on the style of Truman Capote's In Cold Blood. Add title. Use Markdown syntax. E.g title in bold as *title*. E.g italic for thoughts or quotes. VERY IMPORTANT
    - "image": a DALL·E prompt; text description to generate the image on a text-to-image model
    - "available_actions": a list of strings with the available actions for the player to take. It's a very super sentence describing the action.

The resulting JSON is:
"""

CONTINUE_STORY_TEMPLATE = """
This is a game, similar to those old school conversational adventures.

You are the narrator.

The story is always about a crime, the main character (the player) is a person involved somehow in the crime and who has to solve it either because of professional reasons or very strong personal reasons.

The history so far is:

{history}

Consider the last taken action was: {last_action}

Output a JSON with the following fields:
    - "text": the next short paragraph of the story. Narrated on the style of Truman Capote's In Cold Blood. Use Markdown syntax. E.g italic for thoughts or quotes. VERY IMPORTANT
    - "image": a DALL·E prompt; text description to generate the image on a text-to-image model
    - "available_actions": a list of strings with the available actions for the player to take. It's a super short sentence describing the action.

The resulting JSON is:
"""
