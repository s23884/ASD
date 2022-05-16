def partition(BBB, low, high):

  c = BBB[high]

  i = low - 1

  
  for j in range(low, high):
    if BBB[j] <= c:
      
      i = i + 1

      (BBB[i], BBB[j]) = (BBB[j], BBB[i])

  (BBB[i + 1], BBB[high]) = (BBB[high], BBB[i + 1])

  return i + 1

def quick_sort(BBB, low, high):
  if low < high:

    p = partition(BBB, low, high)

    quick_sort(BBB, low, p - 1)

    quick_sort(BBB, p + 1, high)


if __name__ == '__main__':

    tabela1 = [0,1,3,5,7,9,2,4,6,8]
    tabela2 = [6,7,22,34,55,60,5,40,55,1,3]

quick_sort(tabela1, 0, len(tabela1) - 1)
print(tabela1)

quick_sort(tabela2, 0, len(tabela2) - 1)
print(tabela2)
