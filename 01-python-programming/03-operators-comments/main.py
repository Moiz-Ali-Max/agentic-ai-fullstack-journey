
### 2. Assignment Operators
# 1. =
# 2. +=
# 3. -=
# 4. *=
# 5. /=
# 6. %=
# 7. //=
# 8. **=
a : int = 10
print("Here we assign 10 in a thorugh =, so it is = operator: ", a)

a: int = 5
a += 2
print(a)


a: int = 5
a -= 2
print(a)

a: int = 5
a *= 2
print(a)

a: int = 6
a /= 2
print(a)

a: int = 5
a %= 2
print(a)

a: int = 5
a //= 2
print(a)

a: int = 5
a **= 2
print(a)

### 3. Comparison Operators:
# 1. ==
# 2. !=
# 3. greater-than: >
# 4. <
# 5. greater-equal: >=
# 6. <=
a: int = 5
b: str = "seven"
print(a == b)

a: int = 5
b: str = "seven"
print(a != b)

a: int = 5
b: int = 10
print(a > b)

a: int = 5
b: int = 10
print(a < b)

a: int = 5
b: int = 10
print(a >= b)

a: int = 5
b: int = 10
print(a <= b)

### 4. Logical Operators
# 1. and
# 2. or
# 3. not
True and True and True

True or False or True

not True

### 5. Identity Operator
# 1. is
# 2. is not
a: str = "a"
b: str = "b"
print(id(a))
print(id(b))

print(a is b)
print(a is not b)

### 6. Membership Operator
# 1. in
# 2. not in
name: str = "moiz ali afzaal"
print("m" in name)

name: str = "moiz ali afzaal"
print("m" not in name)

### 7. Operator Precendance
##### PEMDAS Rule
# - Paranthesis
# - Exponent
# - Multiplication
# - Division
# - Addition
# - Subtraction
print(3 + 2 - 1 * 9 / 3)

big_nummber: int = 14_000_000_000_000
print(big_nummber)

a, b, c = "a", 10, 1.0
print(a, b, c)

data = ("moiz", 10, 1.0)
print(data[0], data[1], data[2])
print(*data) #for unzip easily

"a" * 10
