# https://ru.stackoverflow.com/q/1184300/176064


def solve(k: int, S: str):
  n = len(S)
  mood = k
  worse_mood = mood
  for i in range(n-1):
      if S[i] == 'C':
          mood -= 1
      elif S[i] == 'A':
          mood += 1

      if mood < worse_mood:
          worse_mood = mood


  if worse_mood < 0:

    return -worse_mood
    
  return 0


def test_data():
  yield  0, 'BCA', 1

  yield  1, 'A',   0
  yield -1, 'C',   1
  yield  0, 'BC',  0
  yield  0, 'BCB', 1
  yield  0, 'BCC', 1
  yield  0, 'BCCB', 2
  yield  -2, 'BCACB', 3
   


if __name__ == '__main__':
  for k, S, expected in test_data():
    result = solve(k, S)
    print(k, S, f'{result}=={expected}', result == expected)