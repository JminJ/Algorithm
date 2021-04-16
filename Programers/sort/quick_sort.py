def quick_sort(a):

  if len(a) <= 1:
    return a

  middle_val = a[len(a) // 2]

  less_arr = []
  equal_arr = []
  greater_arr = []

  for i in range(len(a)):
    if a[i] < middle_val:
      less_arr.append(a[i])
    elif a[i] == middle_val:
      equal_arr.append(a[i])
    else:
      greater_arr.append(a[i])

  less_arr = quick_sort(less_arr)
  greater_arr = quick_sort(greater_arr)

  return less_arr + equal_arr + greater_arr