from misc_helper.nodes.sampler_config import KSamplerAdvancedConfig, KSamplerConfigExtract
from misc_helper.nodes.aspect_ratio import AspectRatioCalculator
from misc_helper.utils.utils import mapNodeClass


NODE_CLASS_MAPPINGS = {
    mapNodeClass(AspectRatioCalculator.NAME): AspectRatioCalculator,
    mapNodeClass(KSamplerAdvancedConfig.NAME): KSamplerAdvancedConfig,
    mapNodeClass(KSamplerConfigExtract.NAME): KSamplerConfigExtract,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    mapNodeClass(AspectRatioCalculator.NAME): AspectRatioCalculator.NAME,
    mapNodeClass(KSamplerAdvancedConfig.NAME): KSamplerAdvancedConfig.NAME,
    mapNodeClass(KSamplerConfigExtract.NAME): KSamplerConfigExtract.NAME,
}
