#1)ახსენით რა არის iteration,sequencing,selection ასევე მოიყვანეთ რეალური მაგალითები ცხოვრებიდან თითოეულთან დაკავშირებით 

#2)შეურიეთ შედარების და ლოგიკური ოპერატორები და გააკეთეთ ისევ 10 მაგალითი 

#3)მომხმარებელს შემოატანინეთ მისი სახელი, შემოატანინეთ მისი ასაკი, ასევე სიმაღლე და შეამოწმეთ თუ მომხმარებლის ასაკი მეტია 18 და მისი სახელი უდრის თქვენს სახელს და ასევე მისი სიმაღლე მეტია 1.80-ზე




for i in range(5):  # 5-ჯერ შესრულდება
    print("Hello!")

print("შეამოწმე საათი")
print("აღდგი წილი")



# Comparison Operators
print(10 == 10)  # True
print(10 != 5)   # True
print(10 > 5)    # True
print(10 < 5)    # False

# Logical Operators
print(10 > 5 and 5 < 20)  # True
print(10 < 5 or 5 < 20)   # True
print(not 10 > 5)         # False



# User Input
user_name = input("სახელი: ")
user_age = int(input("ასაკი: "))
user_height = float(input("სიმაღლე: "))

# Check Conditions
if user_age > 18 and user_name == "გია" and user_height > 1.80:
    print("პირობები შესრულდა!")
else:
    print("პირობები ვერ შესრულდა.")


