
counter = 1
def test2(x):
  print(x)


def test1():
  print(counter)
  test2(counter+1)
  counter = counter+1

test1()