from inspect import cleandoc
from nodes import MAX_RESOLUTION
import comfy.samplers
import math
from misc_helper.utils.utils import getNodeCategory


class PackedConfig:
    def __init__(self, steps, cfg, sampler, scheduler,  steps_start, steps_end, denoise):
        self.steps = steps
        self.cfg = cfg
        self.sampler = sampler
        self.scheduler = scheduler
        self.steps_start = steps_start
        self.steps_end = steps_end
        self.denoise = denoise


class KSamplerAdvancedConfig:
    """ Calculate value for KSamplerAdvanced """

    def __init__(self):
        pass

    NAME = "KSampler Config"
    CATEGORY = getNodeCategory("sampling")

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

    RETURN_TYPES = ("PACKED_CONFIG", )
    RETURN_NAMES = ("packed_config", )
    DESCRIPTION = cleandoc(__doc__)
    FUNCTION = "handle"

    def handle(self, sampler, scheduler, steps, cfg, denoise):
        steps_out = math.floor(steps / max(0.0, min(1.0, denoise)))
        steps_start = steps_out - steps
        steps_end = steps_out

        packed_config = PackedConfig(sampler=sampler, scheduler=scheduler, steps=steps_out, steps_start=steps_start, steps_end=steps_end, cfg=cfg, denoise=denoise)
        return (packed_config, )


class KSamplerConfigExtract:
    """ Extract value from PacketConfig, to feed into KSamplerAdvanced """

    def __init__(self):
        pass

    NAME = "KSampler Config Extract"
    CATEGORY = getNodeCategory("sampling")

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "packed_config": ("PACKED_CONFIG", ),
            },
        }

    RETURN_TYPES = ("INT", "FLOAT", comfy.samplers.KSampler.SAMPLERS, comfy.samplers.KSampler.SCHEDULERS, "INT",  "INT", "FLOAT")
    RETURN_NAMES = ("steps", "cfg", "sampler", "scheduler", "steps_start", "steps_end", "denoise")
    DESCRIPTION = cleandoc(__doc__)
    FUNCTION = "handle"

    def handle(self, packed_config):
        return (packed_config.steps, packed_config.cfg, packed_config.sampler, packed_config.scheduler, packed_config.steps_start, packed_config.steps_end, packed_config.denoise, )
