"""Tests for OME-Zarr file handler."""

from pathlib import Path

import pytest

from croissant_baker.handlers.ome_zarr_handler import OMEZarrHandler


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

ZARR_DEMO = Path(__file__).parent / "data" / "input" / "zarr_demo" / "ome-zarr-0-4.zarr"


@pytest.fixture
def handler() -> OMEZarrHandler:
    return OMEZarrHandler()


# ---------------------------------------------------------------------------
# can_handle
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "name,expected",
    [
        ("image.ome.zarr", True),
        ("image.OME.ZARR", True),
        ("data.zarr", True),  # plain zarr directories should also be handled
        ("image.nii.gz", False),
        ("data.csv", False),
        ("scan.dcm", False),
    ],
)
def test_can_handle(handler: OMEZarrHandler, name: str, expected: bool) -> None:
    assert handler.can_handle(Path(name)) == expected


# ---------------------------------------------------------------------------
# extract_metadata
# ---------------------------------------------------------------------------


def test_extract_metadata_basic(handler: OMEZarrHandler) -> None:
    """Test that extract_metadata returns expected keys for OME-Zarr."""
    meta = handler.extract_metadata(ZARR_DEMO)

    assert meta["file_name"] == "ome-zarr-0-4.zarr"
    assert "ome_zarr_properties" in meta


def test_extract_metadata_multiscales(handler: OMEZarrHandler) -> None:
    """Test that multiscale metadata is extracted."""
    meta = handler.extract_metadata(ZARR_DEMO)
    props = meta["ome_zarr_properties"]

    assert "multiscales" in props
    assert props["ome_zarr_version"] == "0.4"


def test_extract_metadata_axes(handler: OMEZarrHandler) -> None:
    """Test that axes info is extracted."""
    meta = handler.extract_metadata(ZARR_DEMO)
    props = meta["ome_zarr_properties"]

    assert "axes" in props
    # Demo has t, c, z, y, x axes
    axis_names = [a["name"] for a in props["axes"]]
    assert "x" in axis_names
    assert "y" in axis_names


def test_extract_metadata_channels(handler: OMEZarrHandler) -> None:
    """Test that channel info is extracted from omero metadata."""
    meta = handler.extract_metadata(ZARR_DEMO)
    props = meta["ome_zarr_properties"]

    assert "channels" in props
    assert len(props["channels"]) > 0


def test_extract_metadata_file_not_found(handler: OMEZarrHandler) -> None:
    with pytest.raises(FileNotFoundError):
        handler.extract_metadata(Path("/nonexistent/image.zarr"))
