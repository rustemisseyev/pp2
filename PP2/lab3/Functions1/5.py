def permutations(s, step=0):
    if step == len(s):
        print("".join(s))
        return
    for i in range(step, len(s)):
        s_list = list(s)
        s_list[step], s_list[i] = s_list[i], s_list[step]
        permutations(s_list, step + 1)

permutations("asd")