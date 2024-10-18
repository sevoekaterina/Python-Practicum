def check_blockchain(N, blocks):
    prev_hash = 0
    for i in range(N):
        b_n = blocks[i]
        h_n = b_n % 256
        r_n = (b_n // 256) % 256
        m_n = b_n // (256 ** 2)
        expected_hash = (37 * (m_n + r_n + prev_hash)) % 256
        if h_n >= 100 or h_n != expected_hash:
            return i
        prev_hash = h_n
    return -1


N = int(input())
blocks = [int(input()) for _ in range(N)]
result = check_blockchain(N, blocks)
print(result)
