#!/usr/bin/python3

code_type = type(compile("1", "Code", "exec"))

go = input("Code: ")
res = compile(go, "home", "eval")


def clear(code):
    print(">", code.co_names)
    new_consts = []
    print(code.co_consts)
    for const in code.co_consts:
        print("C:", const)
        if isinstance(const, code_type):
            new_consts.append(clear(const))
        elif isinstance(const, int):
            new_consts.append(0)
        elif isinstance(const, str):
            new_consts.append("")
        elif isinstance(const, tuple):
            new_consts.append(tuple(None for _ in range(len(const))))
        else:
            new_consts.append(None)
    return code.replace(co_names=(), co_consts=tuple(new_consts))

res = clear(res)
del clear
del go
del code_type

# Go!
res = eval(res, {}, {})
print(res(vars(), vars))
