from collections import deque

Yagoo_queue = deque()

Yagoo_queue.append("Miko")
Yagoo_queue.append("Suisei")
Yagoo_queue.append("Aqua")

print(f"Origin Team: {Yagoo_queue}")

first_Holomem = Yagoo_queue.popleft()

print(f"{first_Holomem}")

print(f"Now Team: {Yagoo_queue}")

Yagoo_queue.append("Towa")

print(f"Towa join the Team")

print(f"Last Team:{Yagoo_queue}")
