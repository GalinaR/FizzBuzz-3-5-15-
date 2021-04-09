def fizz_buzz(begin, end):
  result = ''
  if begin > end:
    print(result)
  while begin <= end:
    if begin % 3 == 0 and begin % 5 == 0:
      print('FizzBuzz', end = ' ')
    elif begin % 3 == 0:
      print('Fizz', end = ' ')
    elif begin % 5 == 0:
      print('Buzz', end = ' ')
    else:
      print(str(begin), end = ' ')
    begin += 1

fizz_buzz(0, 15)