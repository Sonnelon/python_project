def ValidVeirfy(a):
    stack = []
    verify = True

    for lt in a:
        if lt in "([{":
            stack.append(lt)
        elif lt in ")]}":
            if len(stack) == 0:
                verify = False
                break
            br = stack.pop()
            if br == '(' and lt == ')':
                continue
            if br == '[' and lt == ']':
                continue
            if br == '{' and lt == '}':
                continue

            verify = False
            break

    if verify and len(stack) == 0:
        print("Yes")
    else:
        print("No")

