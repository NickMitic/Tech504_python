frozen_set = frozenset({"hello", "world"})
normal_set = {"let's","learn"}
normal_set.add(frozen_set)
# Non-frozensets are mutable
print(normal_set)