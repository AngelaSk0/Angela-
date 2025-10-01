students = {}  

print("Введіть оцінки студентів (від 1 до 12). Щоб завершити, введіть 'stop'.")

while True:
    name = input("Ім'я студента: ")
    if name.lower() == "stop":
        break

    if name not in ["Vika", "Sasha", "Olecsij", "Valik"]:
        print("Цього студента немає у списку!")
        continue

    try:
        grade = int(input("Оцінка (1-12): "))
        if 1 <= grade <= 12:
            students[name] = grade
        else:
            print("Оцінка має бути від 1 до 12!")
    except ValueError:
        print("Введіть число!")

print("\n--- Результати ---")
for name, grade in students.items():
    print(f"{name}: {grade}")

if students:
    avg = sum(students.values()) / len(students)
    print(f"\nСередній бал по групі: {avg:.2f}")

    vidminnyky = [n for n, g in students.items() if 10 <= g <= 12]
    horoshysty = [n for n, g in students.items() if 7 <= g <= 9]
    vidstayuchi = [n for n, g in students.items() if 4 <= g <= 6]
    nezdaly = [n for n, g in students.items() if 1 <= g <= 3]

    print(f"\nВідмінники ({len(vidminnyky)}): {', '.join(vidminnyky) if vidminnyky else 'немає'}")
    print(f"Хорошисти ({len(horoshysty)}): {', '.join(horoshysty) if horoshysty else 'немає'}")
    print(f"Відстаючі ({len(vidstayuchi)}): {', '.join(vidstayuchi) if vidstayuchi else 'немає'}")
    print(f"Не здали ({len(nezdaly)}): {', '.join(nezdaly) if nezdaly else 'немає'}")
else:
    print("Жодного студента не було введено.")
