# pylint: disable=missing-module-docstring

from pathlib import Path
from unittest.mock import patch

import pytest
from pyheroicons import InvalidVariantError, heroicon

TEST_ICONS = Path(__file__).parent / "icons" / "optimized"


@patch("pyheroicons.ICONS_DIR", new=TEST_ICONS)
def test_heroicon_with_stroke_width():
    """
    Test the heroicon function with an SVG that has an existing stroke-width attribute.
    The function should update the stroke-width to the provided value and set the class attribute.
    """  # noqa: E501
    icon_svg = heroicon(
        "icon_with_stroke", "outline", cls="test-class", strokewidth="2"
    )
    assert 'stroke-width="2"' in icon_svg
    assert 'class="test-class"' in icon_svg


@patch("pyheroicons.ICONS_DIR", new=TEST_ICONS)
def test_heroicon_without_stroke_width():
    """
    Test the heroicon function with an SVG that does not have an existing stroke-width attribute.
    The function should not add a stroke-width attribute and should set the class attribute.
    """  # noqa: E501
    icon_svg = heroicon(
        "icon_without_stroke", "outline", cls="test-class", strokewidth="2"
    )
    assert 'stroke-width="2"' not in icon_svg
    assert 'class="test-class"' in icon_svg


@patch("pyheroicons.ICONS_DIR", new=TEST_ICONS)
def test_heroicon_invalid_variant():
    """
    Test the heroicon function with an invalid variant.
    The function is expected to raise an InvalidVariantError.
    """
    with pytest.raises(InvalidVariantError):
        heroicon("icon_name", "invalid_variant")  # type: ignore


@patch("pyheroicons.ICONS_DIR", new=TEST_ICONS)
def test_heroicon_no_class_no_strokewidth():
    """
    Test the heroicon function with no class and no strokewidth parameters.
    The SVG should be returned without changes to class or stroke-width attributes.
    """  # noqa: E501
    icon_svg = heroicon("icon_with_stroke", "outline")
    assert 'class="' not in icon_svg
    assert 'stroke-width="1.5"' in icon_svg
