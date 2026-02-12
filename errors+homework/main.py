# N1
while True:
    try:
        num1 = float(input("შეიყვანეთ პირველი რიცხვი: "))
        num2 = float(input("შეიყვანეთ მეორე რიცხვი: "))

        result = num1 / num2
        print("გაყოფის შედეგია:", result)
        break

    except ValueError:
        print("შეცდომა: გთხოვთ შეიყვანოთ რიცხვითი მნიშვნელობები!")
    except ZeroDivisionError:
        print("შეცდომა: ნულზე გაყოფა არ შეიძლება!")

# N2

def divide_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "შეცდომა: ნულზე გაყოფა არ შეიძლება!"
    except TypeError:
        return "შეცდომა: არასწორი ტიპის მონაცემი!"

print(divide_numbers(10, 2))
print(divide_numbers(10, 0))
print(divide_numbers(10, "a"))


# N3

numbers = [10, 20, 30]

try:
    index = int(input("შეიყვანეთ ინდექსი: "))
    print("ელემენტი არის:", numbers[index])
except IndexError:
    print("შეცდომა: ასეთი ინდექსი არ არსებობს სიაში!")
except ValueError:
    print("შეცდომა: შეიყვანეთ მთელი რიცხვი!")

# N4

try:
    with open("myresult.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("შეცდომა: ფაილი myresult.txt არ არსებობს!")

# N5

import math

try:
    a = float(input("შეიყვანეთ a: "))
    b = float(input("შეიყვანეთ b: "))
    c = float(input("შეიყვანეთ c: "))

    if a == 0:
        raise ValueError("ეს არ არის კვადრატული განტოლება (a არ უნდა იყოს 0)")

    D = b**2 - 4*a*c

    if D < 0:
        print("ფესვები არ არსებობს (დისკრიმინანტი უარყოფითია)")
    else:
        x1 = (-b + math.sqrt(D)) / (2*a)
        x2 = (-b - math.sqrt(D)) / (2*a)
        print("ფესვები არის:", x1, "და", x2)

except ValueError as e:
    print("შეცდომა:", e)

# N6

try:
    a = int(input("შეიყვანეთ პირველი გვერდი: "))
    b = int(input("შეიყვანეთ მეორე გვერდი: "))
    c = int(input("შეიყვანეთ მესამე გვერდი: "))

    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("ეს რიცხვები არ აკმაყოფილებს სამკუთხედის წესს!")

    average = (a + b + c) / 3
    print("საშუალო არითმეტიკული არის:", average)

except ValueError as e:
    print("შეცდომა:", e)
