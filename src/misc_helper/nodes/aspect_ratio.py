from inspect import cleandoc
import torch
import PIL.Image as Image
from misc_helper.utils.utils import getNodeCategory
from misc_helper.constants import ASPECT_CHOICES
from misc_helper.utils.utils import validateDim


class AspectRatioCalculator:
    """ Use aspect ratio from preset or image, then calculate width and height with a base dimension """

    def __init__(self):
        pass

    NAME = "Aspect Ratio Calculator"
    CATEGORY = getNodeCategory("latent")

    @classmethod
    def INPUT_TYPES(s):
        return {
            "optional": {
                "image": ("Image", {
                    "tooltip": "Extract aspect-ratio from this image"
                }),
            },
            "required": {
                "aspect_ratio": ([lbl for lbl, _ in ASPECT_CHOICES], {
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
            if image == None:
                raise ValueError(f"Unable parse aspect ratio, image was not fed")
            
            if isinstance(image, Image.Image):
                wr, hr = image.size()
            elif isinstance(image, torch.Tensor):
                wr, hr = image.shape[2], image.shape[1]
            else:
                raise ValueError(f"Unknown image type fed into: {image}")

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
            latent = {"samples": torch.zeros(
                [batch_size, 4, h, w], dtype=torch.float32)}
        else:
            latent = None

        return (latent, w, h)
