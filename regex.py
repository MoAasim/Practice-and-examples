import re

text = "This is playground"

res = re.search("^This", text)
if res:
    print(res)
    print("Yes, starts with This")


res2 = re.search("ground$", text)
if res2:
    print(res2)
    print("Yes, ends with ground")