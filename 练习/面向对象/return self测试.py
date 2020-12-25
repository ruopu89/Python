class Foo(object):

  def __init__(self):
    self.myattr = 0

  def bar(self):
    self.myattr += 1
    return self

# f = Foo()
# f.bar().bar().bar()
# print(f.myattr)

a = {'content_list': [{'ext_id': '10002#ABCD0220131127200099', 'usage': 'poster', 'id': 'fc2cb1ce-edbd-4bd1-8e2a-54a82b23b614'}, {'ext_id': '10002#ABCD0320131127200099', 'usage': 'poster', 'id': '5b2d0334-bdd1-44e1-b19e-64c4d4ddfe30'}, {'ext_id': '10002#ABCD0120131127200099', 'usage': 'poster', 'id': '293d5c4e-df3f-479a-b80c-2e7173624854'}, {'ext_id': '10002#ABCD2010000004619572', 'usage': 'movie', 'id': 'e91818c1-8063-4de6-8cb7-fd26bed4b9ca'}]}
print(a['content_list']['id'])
