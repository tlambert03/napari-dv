from typing import TYPE_CHECKING, List, Union

from napari_plugin_engine import napari_hook_implementation

if TYPE_CHECKING:
    from napari.types import LayerDataTuple


@napari_hook_implementation
def napari_get_reader(path):
    if isinstance(path, str) and path.endswith((".dv", ".mrc")):
        return dv_reader


def dv_reader(path: str) -> List["LayerDataTuple"]:
    import mrc

    with mrc.DVFile(path) as dv:
        data = dv.asarray()
        meta = dv.hdr._asdict()
        meta["ext_hdr"] = dv.ext_hdr._asdict() if dv.ext_hdr else {}
        contrast_limits: Union[tuple, list]
        name: Union[str, list]
        if dv.hdr.nc == 1:
            contrast_limits = (dv.hdr.min, dv.hdr.max)
            name = f"{dv.hdr.wave1}nm"
        else:
            contrast_limits = []
            name = []
            for c in range(1, dv.hdr.nc + 1):
                if c == 1:
                    clim = (dv.hdr.min, dv.hdr.max)
                else:
                    min_ = (getattr(dv.hdr, f"min{c}"),)
                    max_ = getattr(dv.hdr, f"max{c}")
                    clim = (min_, max_)
                contrast_limits.append(clim)
                name.append(str(getattr(dv.hdr, f"wave{c}")) + "nm")

        scale = [
            getattr(dv.voxel_size, k.lower(), 1)
            for k, v in dv.sizes.items()
            if v > 1 and k != "C"
        ]
        params = {
            "channel_axis": dv.axes.find("C") if dv.hdr.nc > 1 else None,
            "scale": scale,
            "contrast_limits": contrast_limits,
            "name": name,
            "metadata": meta,
        }
        return [(data, params)]
