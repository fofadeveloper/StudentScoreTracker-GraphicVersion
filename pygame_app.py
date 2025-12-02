# این فایل نسخه گرافیکی پروژه را با استفاده از pygame پیاده سازی می کند
# شامل منوی اصلی، فرم اضافه کردن دانش آموز، ثبت نمره و نمایش لیست است

import pygame
import sys
import storage
from student import Student


pygame.init()

# اندازه پنجره
WIDTH, HEIGHT = 800, 600

# ساخت پنجره اصلی
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Student Score Tracker (Pygame)")

# تعریف فونت ها
FONT = pygame.font.SysFont(None, 40)
SMALL_FONT = pygame.font.SysFont(None, 30)

# تابع کمکی برای رسم متن روی صفحه


def draw_text(text, x, y, color=(0, 0, 0)):
    img = FONT.render(text, True, color)
    screen.blit(img, (x, y))


# تابع کمکی ساخت دکمه(مستطیل + متن)
def draw_button(text, x, y, w, h):
    pygame.draw.rect(screen, (180, 180, 180, 180), (x, y, w, h))
    pygame.draw.rect(screen, (0, 0, 0), (x, y, w, h), 2)
    label = SMALL_FONT.render(text, True, (0, 0, 0))
    screen.blit(label, (x + 10, y + 10))
    return pygame.Rect(x, y, w, h)


# کلاس ساده برای ورودی متن TextBox
class TextBox:
    def __init__(self, x, y, w, h):
        # ایجاد باکس ورودی با مختصات و اندازه
        self.rect = pygame.Rect(x, y, w, h)
        self.text = ""
        self.active = False

    def handle_event(self, event):
        # مدیریت کلیک و تایپ
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.rect.collidepoint(event.pos)

        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]  # حذف آخرین حرف
            else:
                self.text += event.unicode  # افزودن کاراکتر جدید

    def draw(self):
        # رسم مستطیل و متن داخل آن
        pygame.draw.rect(screen, (255, 255, 255), self.rect)
        pygame.draw.rect(screen, (0, 0, 0), self.rect, 2)
        img = SMALL_FONT.render(self.text, True, (0, 0, 0))
        screen.blit(img, (self.rect.x + 5, self.rect.y + 5))


# صفحه اصلی (منو اصلی)
def main_menu():
    while True:
        screen.fill((230, 230, 230))
        draw_text("Main Menu", 320, 50, 300)

        btn_add_student = draw_button("Add Student", 300, 150, 200, 50)
        btn_add_score = draw_button("Add Score", 300, 220, 200, 50)
        btn_list = draw_button("Students List", 300, 290, 200, 50)
        btn_exit = draw_button("Exit", 300, 360, 200, 50)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if btn_add_student.collidepoint(event.pos):
                    add_student_screen()
                if btn_add_score.collidepoint(event.pos):
                    add_score_screen()
                if btn_list.collidepoint(event.pos):
                    list_students_screen()
                if btn_exit.collidepoint(event.pos):
                    sys.exit()

        pygame.display.flip()

# صفحه افزودن دانش آموز


def add_student_screen():
    tb_name = TextBox(250, 200, 300, 40)

    while True:
        screen.fill((230, 230, 230))
        draw_text("Add Student", 330, 100)
        draw_text("Name:", 180, 205)
        tb_name.draw()

        btn_save = draw_button("Save", 250, 300, 120, 50)
        btn_back = draw_button("Back", 430, 300, 120, 50)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            tb_name.handle_event(event)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if btn_save.collidepoint(event.pos):
                    students = storage.load_students()
                    new = Student(tb_name.text)
                    students.append(new.to_dict())
                    storage.save_students(students)
                    return  # بازگشت به منو
                if btn_back.collidepoint(event.pos):
                    return

        pygame.display.flip()


# صفحه افزودن نمره
def add_score_screen():
    tb_name = TextBox(250, 200, 300, 40)
    tb_score = TextBox(250, 260, 300, 40)

    while True:
        screen.fill((230, 230, 230))
        draw_text("Add Score", 330, 100)

        draw_text("Student Name:", 100, 205)
        tb_name.draw()

        draw_text("Score:", 160, 265)
        tb_score.draw()

        btn_save = draw_button("Save", 250, 350, 120, 50)
        btn_back = draw_button("Back", 430, 350, 120, 50)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            tb_name.handle_event(event)
            tb_score.handle_event(event)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if btn_save.collidepoint(event.pos):
                    try:
                        score = float(tb_score.text)
                    except ValueError:
                        return

                    students = storage.load_students()
                    for s in students:
                        if s["name"] == tb_name.text:
                            s["scores"].append(score)
                            storage.save_students(students)
                            return
                    return
                if btn_back.collidepoint(event.pos):
                    return

        pygame.display.flip()


# صفحه نمایش لیست دانش آموزان
def list_students_screen():
    while True:
        screen.fill((230, 230, 230))
        draw_text("Student List", 310, 50)

        students = storage.load_students()

        y = 120
        for s in students:
            avg = sum(s["scores"]) / len(s["scores"]) if s["scores"] else 0
            text = f"{s["name"]} | Scores: {s["scores"]} | Avg: {avg: .2f}"
            line = SMALL_FONT.render(text, True, (0, 0, 0))
            screen.blit(line, (80, y))
            y += 40

        btn_back = draw_button("Back", 340, 500, 120, 50)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if btn_back.collidepoint(event.pos):
                    return

        pygame.display.flip()


# اجرای برنامه گرافیکی
if __name__ == "__main__":
    main_menu()
