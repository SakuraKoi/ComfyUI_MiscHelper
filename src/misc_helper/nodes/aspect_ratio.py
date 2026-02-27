from inspect import cleandoc
import torch
import PIL.Image as Image
from misc_helper.utils.utils import validateDim

ASPECT_CHOICES = [
    ("From image",      (0, 0)),
    # Standard
    ("1:1",             (1, 1)),    # 1
    ("5:4",             (5, 4)),    # 0.8
    ("4:3",             (4, 3)),    # 0.75
    ("7:5",             (7, 5)),    # 0.7142
    ("3:2",             (3, 2)),    # 0.67
    ("16:9",            (16, 9)),   # 0.5625
    ("21:9",            (21, 9)),   # 0.4286
    # Custom
    ("91:64 Postcard",  (91, 64)),  # 0.7033
]

class AspectRatioCalculator:
    """ Use aspect ratio from preset or image, then calculate width and height with a base dimension """
    def __init__(self):
        pass

    NAME = "Aspect Ratio Calculator"
    CATEGORY = "NyakoTech"

    @classmethod
    def INPUT_TYPES(s):
        return {
            "optional": {
                "image": ("Image", { 
                    "tooltip": "Extract aspect-ratio from this image"
                }),
            },
            "required": {
                "aspect_ratio": ([lbl for lbl,_ in ASPECT_CHOICES], {
                    "default": "4:3"
                }),
                "swap_orient": ("BOOLEAN", {
                    "default": False
                }),
                "dimension_px": ("INT", {
                    "default": 512,
                    "min": 128,
                    "max": 8192,
                    "step": 64,
                    "display": "number" 
                }),
                "reference_dim": (["Width", "Height"], {
                    "default": "Height"
                }),
                "batch_size":   ("INT",    {
                    "default": 0,   
                    "min": 0
                }),
            },
        }

    RETURN_TYPES = ("LATENT", "INT", "INT")
    RETURN_NAMES = ("latent", "width", "height")
    DESCRIPTION = cleandoc(__doc__)
    FUNCTION = "handle"


    def handle(self, image, aspect_ratio: str, swap_orient: bool, dimension_px: int, reference_dim: str, batch_size: int):
        validateDim(dimension_px)

        ratio_map = dict(ASPECT_CHOICES)
        if aspect_ratio not in ratio_map:
            raise ValueError(f"Unknown aspect ratio: {aspect_ratio}")
        
        wr, hr = ratio_map[aspect_ratio]

        if wr == 0 and hr == 0:  # calculate from input Image
            if isinstance(image, Image.Image):
                wr, hr = image.size()
            elif isinstance(image, torch.Tensor):
                wr, hr = image.shape[2], image.shape[1]

        if swap_orient:
            wr, hr = hr, wr

        if reference_dim == "Width":
            w, h = dimension_px, round(dimension_px * hr / wr)
        else:
            h, w = dimension_px, round(dimension_px * wr / hr)

        h = h // 8
        w = w // 8

        validateDim(w)
        validateDim(h)
        if batch_size > 0:
            latent = {"samples": torch.zeros([batch_size, 4, h, w], dtype=torch.float32)}
        else:
            latent = None
            
        return (latent, w, h)
