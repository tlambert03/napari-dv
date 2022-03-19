from pathlib import Path

from napari_dv import napari_get_reader

dv_file = Path(__file__).parent / "toxo.dv"


def test_get_reader_hit():
    reader = napari_get_reader(str(dv_file))
    assert reader is not None
    assert callable(reader)
    ((array, params),) = reader(str(dv_file))
    assert array.shape == (2, 17, 128, 128)
    assert params["metadata"]["dvid"] == -16224


def test_get_reader_pass():
    reader = napari_get_reader("fake.file")
    assert reader is None
