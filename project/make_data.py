import csv
import hashlib
from pathlib import Path

# Отримуємо абсолютний шлях до папки project/data
DATA_DIR = Path(__file__).resolve().parent / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)


def get_hash(i: int) -> str:
  return hashlib.md5(str(i).encode()).hexdigest()[:8]


# 1. Створення member.csv
with open(DATA_DIR / "member.csv", "w", newline="", encoding="utf-8") as f:
  writer = csv.writer(f)
  for i in range(1, 1001):
    writer.writerow([
        i,
        f"Member_{i}",
        f"user_{i}_{get_hash(i)}@example.com",
        "Київ" if i % 2 == 0 else "Львів",
        "2024-01-15",
    ])

# 2. Створення workout.csv
with open(DATA_DIR / "workout.csv", "w", newline="", encoding="utf-8") as f:
  writer = csv.writer(f)
  kinds = ["Силові", "Кардіо", "Йога", "Кросфіт", "Пілатес"]
  for i in range(1, 51):
    writer.writerow([
        i,
        f"WK-{i:04d}",
        f"Тренування {i}",
        kinds[i % len(kinds)],
        150.00 + (i * 10),
    ])

# 3. Створення visit.csv
with open(DATA_DIR / "visit.csv", "w", newline="", encoding="utf-8") as f:
  writer = csv.writer(f)
  for i in range(1, 1001):
    writer.writerow([
        i,
        ((i * 17) % 1000) + 1,
        ((i * 31) % 50) + 1,
        1,
        200.00,
        "attended",
        "2024-02-01 10:00:00",
        f"Start note {i}",
    ])

print(f"Дані успішно записано у папку: {DATA_DIR}")