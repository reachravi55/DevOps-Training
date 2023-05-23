"""lines = []
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break

text = '\n'.join(lines)

print (text)"""
contents = []
while True:
    try:
        line = input()
        if line:
            contents.append(line + '\n')
        else:
            break
    except EOFError:
        break
text = "\n".join(contents)
print(text)

