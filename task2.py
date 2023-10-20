
text1 = input("Текст: ").lower()

golosni = "aeiou"
count = 0

for char in text1:
    if char in golosni:
        count = count+1

print("Голосних у тексті:", count)

