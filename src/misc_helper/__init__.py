from misc_helper.nodes.sampler_config import KSamplerAdvancedConfig, KSamplerConfigExtract
from misc_helper.nodes.aspect_ratio import AspectRatioCalculator

def get_node_class(name):
    return "nyakotech:{}".format(name.lower().replace(" ", "_"))

NODE_CLASS_MAPPINGS = {
    get_node_class(AspectRatioCalculator.NAME): AspectRatioCalculator,
    get_node_class(KSamplerAdvancedConfig.NAME): KSamplerAdvancedConfig,
    get_node_class(KSamplerConfigExtract.NAME): KSamplerConfigExtract,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    get_node_class(AspectRatioCalculator.NAME): AspectRatioCalculator.NAME,
    get_node_class(KSamplerAdvancedConfig.NAME): KSamplerAdvancedConfig.NAME,
    get_node_class(KSamplerConfigExtract.NAME): KSamplerConfigExtract.NAME,
}
