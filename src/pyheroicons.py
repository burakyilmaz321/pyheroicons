"""
This module provides a utility for generating SVG Heroicon templates based on provided parameters.
"""  # noqa: E501

from pathlib import Path
from typing import Literal, Optional, get_args
from xml.etree import ElementTree

Variant = Literal["outline", "solid", "mini", "micro"]
ICONS_DIR = Path(__file__).parent.parent / "icons" / "optimized"


def heroicon(
    name: str,
    variant: Variant,
    cls: Optional[str] = None,
    strokewidth: Optional[str] = None,
) -> str:
    """
    This function modifies the SVG file by setting the 'class' attribute and optionally
    updating the 'stroke-width' attribute. The 'stroke-width' attribute is only modified
    if it already exists in the SVG and a 'strokewidth' argument is provided.

    Args:
        name (str): Name of the Heroicon.
        variant (Variant): Variant of the icon ('outline', 'solid', 'mini', 'micro').
        cls (str, optional): Class attribute to be set in the SVG. Defaults to None.
        strokewidth (str, optional): Value to set for the 'stroke-width' attribute. This
                                     parameter is only used if the SVG originally contains
                                     a 'stroke-width' attribute. Defaults to None.

    Returns:
        str: A string representation of the modified SVG.

    Raises:
        InvalidVariantError: If an invalid icon variant is provided.
    """  # noqa: E501
    if variant == "outline":
        path = ICONS_DIR / "24" / "outline" / f"{name}.svg"
    elif variant == "solid":
        path = ICONS_DIR / "24" / "solid" / f"{name}.svg"
    elif variant == "mini":
        path = ICONS_DIR / "20" / "solid" / f"{name}.svg"
    elif variant == "micro":
        path = ICONS_DIR / "16" / "solid" / f"{name}.svg"
    else:
        raise InvalidVariantError

    # Parse SVG file
    ElementTree.register_namespace("", "http://www.w3.org/2000/svg")
    tree = ElementTree.parse(path)
    root = tree.getroot()

    # Set or modify the 'class' attribute
    if cls is not None:
        root.set("class", cls)

    # Check if 'stroke-width' exists, then set or modify it
    if strokewidth is not None:
        if root.get("stroke-width"):
            root.set("stroke-width", strokewidth)

    return ElementTree.tostring(root, encoding="unicode")


class InvalidVariantError(Exception):
    """
    Custom exception raised when an invalid icon variant is provided.
    """

    def __init__(self):
        """
        Initialize the exception.
        """
        valid_options = ", ".join(get_args(Variant))
        message = f"Invalid variant. Expected one of: {valid_options}."
        super().__init__(message)
