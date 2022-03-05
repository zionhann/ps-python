e, s, m = map(int, input().split())
e_ = s_ = m_ = y = 1

while True:
    if e == e_ and s == s_ and m == m_:
        print(y)
        break
    else:
        y += 1
        e_ += 1 if e_ < 15 else -e_ + 1
        s_ += 1 if s_ < 28 else -s_ + 1
        m_ += 1 if m_ < 19 else -m_ + 1
