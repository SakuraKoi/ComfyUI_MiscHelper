from inspect import cleandoc
from nodes import MAX_RESOLUTION
import comfy.samplers
import math

class KSamplerAdvancedConfig:
    """ Calculate value for KSamplerAdvanced """
    def __init__(self):
        pass

    NAME = "KSampler Config"
    CATEGORY = "NyakoTech"

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "sampler": (comfy.samplers.KSampler.SAMPLERS,),
                "scheduler": (comfy.samplers.KSampler.SCHEDULERS,),
                "steps": ("INT", {
                    "default": 30,
                    "min": 1,
                    "max": MAX_RESOLUTION,
                    "step": 1,
                }),
                "cfg": ("FLOAT", {
                    "default": 7.0,
                    "min": 0.0,
                    "max": 100.0,
                    "step": 0.05,
                }),
                "denoise": ("FLOAT", {
                    "default": 1.0,
                    "min": 0.0,
                    "max": 1.0,
                    "step": 0.01,
                }),
            },
        }

    RETURN_TYPES = (comfy.samplers.KSampler.SAMPLERS, comfy.samplers.KSampler.SCHEDULERS, "INT", "INT", "INT", "FLOAT")
    RETURN_NAMES = ("sampler", "scheduler", "steps", "steps_start", "steps_end", "cfg")
    DESCRIPTION = cleandoc(__doc__)
    FUNCTION = "handle"


    def handle(self, sampler, scheduler , steps, cfg, denoise):
        steps_start = math.floor(steps * (1 - denoise))
        return (sampler, scheduler, steps, steps_start, MAX_RESOLUTION, cfg)
