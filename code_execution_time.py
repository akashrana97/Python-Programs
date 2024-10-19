from timeit import repeat, timeit

list_comp: str = """my_list:list[int] = [i for i in range(10)]"""
for_loop: str = """
my_list: list[int] = []
for i in range(10):
    my_list.append(i)
"""
# repeat test code five time
# list_comp_time: float = min(repeat(list_comp, repeat=5, number=1_000_000))
# for_loop_time: float = min(repeat(for_loop, repeat=5, number=1_000_000))

# timeit test code one time only
list_comp_time: float = timeit(list_comp, number=1_000_000)
for_loop_time: float = timeit(for_loop, number=1_000_000)

print(f"List comp: {list_comp_time:.3f}s")
print(f"For Loop: {for_loop_time:.3f}s")