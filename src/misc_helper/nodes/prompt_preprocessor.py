
from inspect import cleandoc

from misc_helper.utils.utils import getNodeCategory


class PromptPreprocessor:
    """ Cleanup tag based prompt text, remove extra spaces, newlines, etc. """

    def __init__(self):
        pass

    NAME = "Tag Prompt Preprocessor"
    CATEGORY = getNodeCategory("prompt")

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "prompt_text": ("STRING", {"forceInput": True} ),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("prompt_text",)
    DESCRIPTION = cleandoc(__doc__)
    FUNCTION = "handle"

    def handle(self, prompt_text):
        prompt_text = prompt_text.strip()
        prompt_text = prompt_text.replace('\n', ' ').replace('\r', ' ')
        prompt_text = prompt_text.replace(',', ', ').replace("\, ", "\,")
        prompt_text = prompt_text.rstrip(', ')
        prompt_text = ' '.join(prompt_text.split())
        return (prompt_text)
