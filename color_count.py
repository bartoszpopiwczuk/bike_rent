from collections import Counter

from PIL import Image

# Wczytaj obraz
img = Image.open("stary_200_20.jpg")

# Konwertuj na RGB (dla pewności, że nie ma kanału alfa)
img = img.convert("RGB")

# Pobierz wszystkie piksele
pixels = list(img.getdata())

# Policz wystąpienia każdego koloru
color_counts = Counter(pixels)

print("=== Oryginalne kolory ===")
for color, count in color_counts.most_common(20):  # wyświetlam tylko 10 najczęstszych
    print(f"Kolor rgb{color}: {count} pikseli")


# Funkcja do uproszczenia kolorów
def simplify_color(rgb, step=2):
    return tuple((c // step) * step for c in rgb)


# Scalanie podobnych kolorów
merged = Counter()
for color, count in color_counts.items():
    merged[simplify_color(color, step=2)] += count

print("\n=== Uproszczone kolory ===")
for color, count in merged.most_common(20):
    print(f"Kolor rgb{color}: {count} pikseli")


# === Oryginalne kolory ===
# Kolor rgb(34, 38, 37): 2815 pikseli
# Kolor rgb(87, 115, 155): 2374 pikseli
# Kolor rgb(60, 83, 135): 1748 pikseli
# Kolor rgb(66, 72, 72): 1623 pikseli
# Kolor rgb(115, 136, 153): 1616 pikseli
# Kolor rgb(94, 115, 134): 1521 pikseli
# Kolor rgb(73, 90, 118): 1225 pikseli
# Kolor rgb(145, 163, 163): 1197 pikseli AQUA
# Kolor rgb(117, 132, 127): 1110 pikseli
# Kolor rgb(34, 40, 62): 1059 pikseli
# Kolor rgb(171, 177, 149): 991 pikseli
# Kolor rgb(52, 66, 92): 958 pikseli
# Kolor rgb(52, 74, 147): 940 pikseli
# Kolor rgb(36, 51, 108): 915 pikseli
# Kolor rgb(113, 141, 180): 876 pikseli
# Kolor rgb(77, 109, 168): 800 pikseli
# Kolor rgb(67, 66, 48): 705 pikseli SAND YELLOW
# Kolor rgb(137, 143, 117): 526 pikseli 
# Kolor rgb(175, 177, 114): 522 pikseli
# Kolor rgb(178, 163, 62): 221 pikseli

# === Uproszczone kolory ===
# Kolor rgb(34, 38, 36): 2815 pikseli
# Kolor rgb(86, 114, 154): 2722 pikseli
# Kolor rgb(60, 82, 134): 1821 pikseli
# Kolor rgb(114, 136, 152): 1715 pikseli
# Kolor rgb(66, 72, 72): 1703 pikseli
# Kolor rgb(94, 114, 134): 1521 pikseli
# Kolor rgb(144, 162, 162): 1230 pikseli
# Kolor rgb(72, 90, 118): 1225 pikseli
# Kolor rgb(34, 40, 62): 1154 pikseli
# Kolor rgb(116, 132, 126): 1145 pikseli
# Kolor rgb(52, 66, 92): 1054 pikseli
# Kolor rgb(170, 176, 148): 1022 pikseli
# Kolor rgb(112, 140, 180): 944 pikseli
# Kolor rgb(52, 74, 146): 940 pikseli
# Kolor rgb(36, 50, 108): 915 pikseli
# Kolor rgb(76, 108, 168): 803 pikseli
# Kolor rgb(66, 66, 48): 707 pikseli
# Kolor rgb(136, 142, 116): 547 pikseli
# Kolor rgb(174, 176, 114): 522 pikseli
# Kolor rgb(178, 162, 62): 221 pikseli
