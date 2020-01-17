import re
string = "Main aim to start a TECHNICAL BLOG was to keep a place where I can store all my notes, online. Since I have enrolled in quite a few courses, I decided to share whatever I am learning. When I am already making notes, why not share it? So here I am."
print(string)
print()
new = re.sub('[A-Z]','',string)
print(new)
print()
