# تست ذخیره سازی JSON با tmp_path و monkeypatch

from storage import load_students, save_students


def test_storage(tmp_path, monkeypatch):
    # جایگزینی مسیر اصلی با مسیر موقت
    fake_file = tmp_path / "students.json"
    monkeypatch.setattr("storage.DATA_FILE", str(fake_file))

    sample = [
        {
            "name": "Sara",
            "scores": [20, 30]
        }
    ]

    save_students(sample)
    loaded = load_students()
    assert loaded == sample
