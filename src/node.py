from .nodes.aspect_ratio import AspectRatioCalculator

def get_node_class(name):
    return "nyakotech:{}".format(name.lower().replace(" ", "_"))

NODE_CLASS_MAPPINGS = {
    get_node_class(AspectRatioCalculator.NODE_NAME): AspectRatioCalculator
}

NODE_DISPLAY_NAME_MAPPINGS = {
    get_node_class(AspectRatioCalculator.NODE_NAME): AspectRatioCalculator.NODE_NAME
}
