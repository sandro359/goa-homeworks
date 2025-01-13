#შექმენით 10 ცვლადი და მიანიჭთ მნიშვნელობები მაგალითებით (მაგალითად 7 > 9) და შემდეგ დაპრინტეთ True და False სხვა და სხვა კომბინაციით (კომენტარებით მიუწერეთ გვერდით რას გამოიტანს ეკრანზე)


# ცვლადები და მათივე მნიშვნელობები
a, b, c, d, e = 7 > 9, 10 == 10, 5 != 3, 8 < 6, 4 >= 4
f, g, h, i, j = "apple" == "banana", 12 > 5, 20 <= 20, 15 == 15, not (5 < 3)

# კომბინაციები და მათი გამოთვლები:
print(a and b)  # False
print(c or d)   # True
print(e and f)  # False
print(g or h)   # True
print(i and j)  # True
print(a or b)   # True
print(d and e)  # False
print(f or g)   # True
print(h and i)  # True
print(j or c)   # True
