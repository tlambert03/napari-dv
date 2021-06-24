from napari_plugin_engine import napari_hook_implementation
from mrc import imsave


@napari_hook_implementation
def napari_write_image(path, data, meta):
    if not path.endswith((".mrc", ".dv")):
        return None
    imsave(path, data)  # TODO: add metadata
