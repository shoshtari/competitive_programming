def find_lower_bound(arr, target):
    # Find the index of the first element in arr that is >= target
    low, high = 0, len(arr)
    while low < high:
        mid = (low + high) // 2
        if mid == low:
            return low if arr[low] >= target else high
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid
    return low


def calc(a, b, c, d):
    # Return Sum of min(a[i] + c[j], b[i] + d[j]) for i from 0 to n-1 and j from 0 to n-1
    # using min decomposition using abs
    n = len(a)
    sig1 = 0
    for i in range(n):
        sig1 += a[i] + b[i] + c[i] + d[i]

    sig1 *= n

    sig2 = 0
    x = [a[i] - c[i] for i in range(n)]
    y = [b[i] - d[i] for i in range(n)]
    y.sort()
    pary = [y[0]]
    for i in range(1, n):
        pary.append(pary[i - 1] + y[i])

    for i in range(n):
        lower_bound = find_lower_bound(y, -x[i])  # y[lower_bound] >= -x[i]
        if lower_bound == 0:
            assert y[0] >= -x[i]
            sig2 += (x[i] * n) + pary[n - 1]
        elif lower_bound == n:
            assert y[n - 1] < -x[i]
            sig2 += -(x[i] * n + pary[n - 1])
        else:
            assert y[lower_bound - 1] < -x[i] <= y[lower_bound]
            first_half = pary[lower_bound - 1]
            second_half = pary[n - 1] - first_half
            first_half_size = lower_bound
            second_half_size = n - lower_bound
            sig2 += (
                -(x[i] * first_half_size + first_half)
                + (x[i] * second_half_size)
                + second_half
            )
    return (sig1 - sig2) // 2


def solve():
    n = int(input())
    a = input()
    b = input()
    para0 = []
    parb0 = []
    para1 = []
    parb1 = []
    for i in range(n):
        last = 0 if i == 0 else para0[i - 1]
        if a[i] == "0":
            last += 1
        para0.append(last)
        para1.append(i + 1 - last)

        last = 0 if i == 0 else parb0[i - 1]
        if b[i] == "0":
            last += 1
        parb0.append(last)
        parb1.append(i + 1 - last)

    ans = calc(para0, parb0, para1, parb1)
    print(ans)


for _ in range(int(input())):
    solve()
