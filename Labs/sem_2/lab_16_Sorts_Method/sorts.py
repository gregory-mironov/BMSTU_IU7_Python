def shell_sort(array):
    step = len(array) // 2
    while step > 0:
        insertion_sort(array, step)
        step //= 2

def shell_sort_hibbart_1963(array):
    max_step = len(array)
    step = 1
    while step < max_step:
        step <<= 1

    step = (step >> 1) - 1

    while step > 0:
        insertion_sort(array, step)
        step //= 2

def shell_sort_stasevich_1965(array):
    max_step = len(array)
    step = 1
    while step < max_step:
        step <<= 1

    step = (step >> 1) + 1

    while step > 0:
        insertion_sort(array, step)
        step //= 2

def shell_sort_knuth_1973(array):
    max_step = (len(array) + 2) // 3 + 1
    steps = []
    i = 1

    cur = (3 ** i - 1) // 2
    while cur < max_step:
        steps.append(cur)
        i += 1
        cur = (3 ** i - 1) // 2

    for k in range(len(steps) - 1, -1, -1):
        insertion_sort(array, steps[k])

def shell_sort_sedgwick_1982(array):
    max_step = (len(array) + 2) // 3 + 1
    steps = [1]

    pow4 = 4
    pow2 = 1
    
    cur = pow4 + 3 * pow2 + 1
    while cur < max_step:
        steps.append(cur)
        pow4 *= 4
        pow2 *= 2
        cur = pow4 + 3 * pow2 + 1 # 4 ** i + 3 * 2 ** (i - 1) + 1

    for k in range(len(steps) - 1, -1, -1):
        insertion_sort(array, steps[k])

def shell_sort_sedgwick_1986(array):
    max_step = (len(array) + 2) // 3 + 1
    steps = [1]
    i = 1

    while steps[i - 1] < max_step:
        if i % 2 == 0:
            steps.append(9 * (1 << i) - 9 * (1 << (i // 2)) + 1)
        else:
            steps.append(8 * (1 << i) - 6 * (1 << ((i + 1) // 2)) + 1)
        i += 1

    for k in range(len(steps) - 1, -1, -1):
        insertion_sort(array, steps[k])

def shell_sort_fib(array):
    max_step = (len(array) + 1) // 2 + 1
    steps = [1, 1]

    i = 1
    while steps[i] + steps[i - 1] <= max_step:
        steps.append(steps[i] + steps[i - 1])
        i += 1

    for step in range(len(steps) - 1, 0, -1):
        insertion_sort(array, step)

def shell_sort_tokuda_1992(array):
    max_step = (len(array) + 1) // 2 + 1
    i = 0
    steps = [1]
    while steps[i] < max_step:
        i += 1
        steps.append( int((9 * (9 / 4) ** (i - 1) - 4) / 5) )
    
    for k in range(len(steps) - 1, -1, -1):
        insertion_sort(array, steps[k])

def insertion_sort(array, gap):
    for i in range(gap, len(array)):
        val = array[i]
        j = i
        while j >= gap and array[j - gap] > val:
            array[j] = array[j - gap]
            j -= gap
        array[j] = val

def shell_sort_5_11(array):
    step = (len(array) + 1) // 2 + 1
    steps = []
    while step >= 1:
        steps.append(step)
        step = 1 if step == 2 else step * 5 // 11

    for step in steps:
        insertion_sort(array, step)

def shell_sort_3_pow(array):
    max_step = (len(array) + 2) // 3 + 1
    steps = []
    step = 1
    while step < max_step:
        steps.append(step)
        step *= 3

    for k in range(len(steps) - 1, -1, -1):
        insertion_sort(array, steps[k])

def shell_sort_5_pow(array):
    max_step = (len(array) + 4) // 5 + 1
    steps = []
    step = 1
    while step < max_step:
        steps.append(step)
        step *= 5

    for k in range(len(steps) - 1, -1, -1):
        insertion_sort(array, steps[k])
