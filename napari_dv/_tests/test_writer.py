from napari_dv import napari_write_image
import numpy as np


def test_writer(tmpdir):
    path = tmpdir / "out.dv"
    assert not path.exists()
    napari_write_image(str(path), np.zeros((256, 256), dtype=np.float32), {})
    assert path.exists()
