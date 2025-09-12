def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    station = list(map(int, data[1:1+n]))
    r = int(data[1+n])
    k = int(data[1+n+1])
    
    # 计算前缀和
    pref = [0] * (n+1)
    for i in range(1, n+1):
        pref[i] = pref[i-1] + station[i-1]
        
    cov = [0] * n
    for i in range(n):
        left = max(0, i - r)
        right = min(n-1, i + r)
        cov[i] = pref[right+1] - pref[left]
        
    low = min(cov)
    high = low + k + 1
    ans = low
    
    while low <= high:
        mid = (low + high) // 2
        diff = [0] * (n+1)
        need = 0
        cur_inc = 0
        valid = True
        for i in range(n):
            cur_inc += diff[i]
            total = cov[i] + cur_inc
            if total < mid:
                t = mid - total
                need += t
                if need > k:
                    valid = False
                    break
                # 选择最远的站：j = i + r，但不能超过n-1
                j = i + r
                if j >= n:
                    j = n-1
                cur_inc += t   # 当前区域i立即增加t
                end_index = i + 2*r + 1
                if end_index < n:
                    diff[end_index] -= t
        if valid and need <= k:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
            
    print(ans)

if __name__ == "__main__":
    main()