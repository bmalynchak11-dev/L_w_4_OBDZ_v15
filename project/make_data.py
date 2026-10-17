import csv
import hashlib
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)


def get_hash(i: int) -> str:
  return hashlib.md5(str(i).encode()).hexdigest()[:8]


# 1. trainer.csv
with open(DATA_DIR / "trainer.csv", "w", newline="", encoding="utf-8") as f:
  writer = csv.writer(f)
  for i in range(1, 21):
    writer.writerow([i, f"Тренер_{i}", "Фітнес", f"+38050000{i:04d}"])

# 2. workout_room.csv
with open(
    DATA_DIR / "workout_room.csv", "w", newline="", encoding="utf-8"
) as f:
  writer = csv.writer(f)
  for i in range(1, 11):
    writer.writerow([i, f"Зал_{i}", 30])

# 3. membership_plan.csv
with open(
    DATA_DIR / "membership_plan.csv", "w", newline="", encoding="utf-8"
) as f:
  writer = csv.writer(f)
  for i in range(1, 6):
    writer.writerow([i, f"Тариф_{i}", 30 * i, 500.00 * i])

# 4. member.csv
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

# 5. workout.csv
with open(DATA_DIR / "workout.csv", "w", newline="", encoding="utf-8") as f:
  writer = csv.writer(f)
  kinds = ["Силові", "Кардіо", "Йога", "Кросфіт", "Пілатес"]
  for i in range(1, 51):
    trainer_id = (i % 20) + 1
    writer.writerow([
        i,
        f"WK-{i:04d}",
        f"Тренування {i}",
        kinds[i % len(kinds)],
        150.00 + (i * 10),
        trainer_id,
    ])

# 6. visit.csv
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
    ])

print("Усі початкові CSV створено.")