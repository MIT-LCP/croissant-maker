"""OME-Zarr handler for multiscale bioimaging data (Zarr v2)."""

from pathlib import Path

from croissant_baker.handlers.base_handler import FileTypeHandler


class OMEZarrHandler(FileTypeHandler):
    """
    Handler for OME-Zarr stores (.zarr directories, Zarr v2 format).

    OME-Zarr is a specification for storing multiscale bioimaging data
    in Zarr format. This handler currently supports Zarr v2 only (OME-Zarr 0.4).
    """

    EXTENSIONS = (".zarr",)
    FORMAT_NAME = "OME-Zarr"
    FORMAT_DESCRIPTION = "OME-Zarr multiscale bioimaging data (Zarr v2, OME-Zarr 0.4)"

    def can_handle(self, file_path: Path) -> bool:
        """
        Check if path is a .zarr directory with Zarr v2 format.

        Zarr v2 is identified by presence of .zgroup or .zarray at root.
        """
        name = file_path.name.lower()
        if not (name.endswith(".zarr") or name.endswith(".ome.zarr")):
            return False

        # For actual directories, check for Zarr v2 markers
        if file_path.is_dir():
            return (file_path / ".zgroup").exists() or (file_path / ".zarray").exists()

        # For path-based detection (file doesn't exist yet), accept by extension
        return True

    def extract_metadata(self, file_path: Path, **kwargs) -> dict:
        """Extract metadata from an OME-Zarr store."""
        if not file_path.exists():
            raise FileNotFoundError(f"OME-Zarr store not found: {file_path}")

        raise NotImplementedError("extract_metadata not yet implemented")

    def build_croissant(
        self, file_metas: list[dict], file_ids: list[str]
    ) -> tuple[list, list]:
        """Build Croissant FileSets and RecordSets for OME-Zarr stores."""
        raise NotImplementedError("build_croissant not yet implemented")
