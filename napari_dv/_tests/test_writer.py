import numpy as np

from napari_dv import napari_write_image


def test_writer(tmpdir):
    path = tmpdir / "out.dv"
    assert not path.exists()
    napari_write_image(str(path), np.zeros((256, 256), dtype=np.float32), {})
    assert path.exists()
