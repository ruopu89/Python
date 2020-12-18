class A:
    X = 123
    def __init__(self):
        self.y = 5
        pass

# print(sorted(dir(A)))
# print(sorted(A.__dict__))
# =================================================
class B(A):
    def __dir__(self):
        return ['abcdef']

# print('B = ', sorted(dir(B)))
# print(sorted(B.__dict__))

b = B()
# print(sorted(dir(b)))
# print(sorted(b.__dict__))

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print(sorted(set(b.__dict__.keys()) | set(b.__class__.__dict__.keys()) | set(object.__dict__)))