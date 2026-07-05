s = input()
if "." in s:
    dot_index = s.index(".")
    before_dot = s[:dot_index]
    after_dot = s[dot_index:]
    
    words = before_dot.split()
    rev_before = ""
    for word in words:
        rev_before += word[::-1] + " "
    rev_before = rev_before.strip()
    
    rev_after = after_dot[::-1]
    result = rev_before + " " + rev_after
    print(result.strip())
else:
    words = s.split()
    result = ""
    for word in words:
        result += word[::-1] + " "
    print(result.strip())