from .nodes.sampler_config import KSamplerAdvancedConfig
from .nodes.aspect_ratio import AspectRatioCalculator

def get_node_class(name):
    return "nyakotech:{}".format(name.lower().replace(" ", "_"))

NODE_CLASS_MAPPINGS = {
    get_node_class(AspectRatioCalculator.NAME): AspectRatioCalculator,
    get_node_class(KSamplerAdvancedConfig.NAME): KSamplerAdvancedConfig,
}