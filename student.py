# این فایل مدل اصلی پروژه است: یک دانش آموز با نام و لیست نمره ها
# تمام عملیات مربوط به محاسبه میانگین و مدیریت نمره ها در اینجا انجام می شود

class Student:
    """Represents a student with a name and a list of scores"""
    # این کلاس یک دانش آموز را نمایش می دهد

    def __init__(self, name):
        # سازنده کلاس فقط نام دانش آموز را می گیرد
        # و یک لیست خالی نمره ایجاد می کند
        self.name = name
        self.scores = []

    def add_score(self, score):
        """Add a score to the list."""
        # یک نمره جدید به لیست نمره ها اضافه می کند
        self.scores.append(score)

    @property
    def average(self):
        """Return average score."""
        # میانگین نمره ها را بر می گرداند؛
        # اگر لیست خالی بود مقدار 0 بر می گرداند
        if not self.scores:
            return 0
        return sum(self.scores) / len(self.scores)

    def to_dict(self):
        """Convert student to dictionary for JSON saving."""
        # این تابع ساختار را برای ذخیره سازی JSON آماده می کند
        return {
            "name": self.name,
            "scores": self.scores
        }
