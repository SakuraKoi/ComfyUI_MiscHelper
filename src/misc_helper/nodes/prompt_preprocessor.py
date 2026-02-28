
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
        out = prompt_text.strip()
        out = out.replace('\n', ' ').replace('\r', ' ')
        out = out.replace(',', ', ').replace("\, ", "\,")
        out = out.rstrip(', ')
        out = ' '.join(out.split())
        return (out, )
