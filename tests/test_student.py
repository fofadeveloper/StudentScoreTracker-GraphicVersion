# تست های مربوط به کلاس Student

from student import Student


def test_add_score():
    # تست اضافه شدن نمره به دانش آموز
    s = Student("Fazel")
    s.add_score(80)
    assert s.scores == [80]


def test_average():
    # تست محاسبه میانگین
    s = Student("Ali")
    s.add_score(10)
    s.add_score(20)
    assert s.average == 15
