from napari_plugin_engine import napari_hook_implementation


@napari_hook_implementation
def napari_get_reader(path):
    if isinstance(path, str) and path.endswith((".dv", ".mrc")):
        return dv_reader


def dv_reader(path: str):
    from numpy import memmap
    import mrc

    mfile = mrc.Mrc(path)
    nWaves = mfile.header.NumWaves
    channel_axis = mfile.axisOrderStr().find("w") if nWaves > 1 else None
    dx = mfile.header.d[0]
    dz = mfile.header.d[2]
    metadata = {
        name: getattr(mfile.hdr, name)
        for name in mrc.mrc.mrcHdrNames
        if not name.startswith("_")
    }
    metadata = {
        k: v.tolist() if isinstance(metadata["mst"], memmap) else v
        for k, v in metadata.items()
    }
    if nWaves == 1:
        contrast_limits = list(mfile.header.mmm1[:2])
        name = f"{mfile.hdr.wave[0]} nm"
    else:
        contrast_limits = []
        name = []
        for c in range(nWaves):
            key = f"mmm{c+1}" if c == 0 else f"mm{c+1}"
            contrast_limits.append(list(getattr(mfile.header, key)[:2]))
            name.append(f"{mfile.hdr.wave[c]} nm")
    params = {
        "channel_axis": channel_axis,
        "scale": [dz / dx, 1, 1],
        "contrast_limits": contrast_limits,
        "name": name,
        "metadata": metadata,
    }
    return [(mfile.data, params)]
