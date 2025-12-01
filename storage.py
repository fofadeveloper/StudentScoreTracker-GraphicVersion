# ماژول ذخیره سازی JSON
# عملیات لود کردن و ذخیره کردن در فایل students.json را مدیریت می کند

import json
import os

# ساخت مسیر کامل و درست فایل JSON
DATA_FILE = os.path.join(os.path.dirname(__file__), "data", "students.json")


def load_students():
    """Load student list from JSON file"""
    # اگر فایل وجود نداشت یا خراب بود ، لیست خالی برگردان
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []


def save_students(students):
    """Save student list to JSON"""
    # لیست دانش آموزان را در فایل JSON ذخیره می کند
    with open(DATA_FILE, 'w') as f:
        json.dump(students, f, indent=2)
