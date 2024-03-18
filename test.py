# pa = "-23"
# ta = int(pa)
# print(ta)


# all_a = []
# for i in range(10):
#     b = [i, i + 1, i + 2]
#     all_a.append(b)
# print(all_a)

a = ["114514", 1919810, "I have a dream."]
with open("test_output.txt", 'w') as f:
    for item in a:
        f.write(str(item) + "\n")


bb = {}
bb['dwa'] = 2
