StudentScoreTracker

A dual-version Python project (CLI + Pygame GUI) for managing students and their scores.
Bult as a structured educational project following concepts from Python Crash Course.

Features
. Add students
. Add scores
. Calculate averages
. JSON local storage
. CLI interface
. Full Pygame graphical interface
. Pytest unit tests
. Clean multi-file architecture

Project Structure
StudentScoreTracker/
|__app.py(CLI version)
|__pygame_app.py(Graphical version)
|__student.py
|__storage.py
|
|__data/
    |__student.json
|
|__tests/
    |__test_student.py
    |__test_storage.py

RUN CLI version
python app.py

Run graphical version
python pygame_app.py

Run tests
python -m pytest -v

Requirements
.Python 3.12
.Pygame
.Pytest

Install dependencies:
pip install pygame pytest