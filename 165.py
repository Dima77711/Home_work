def palindrom(s):
    if s[::1] == s[::-1]:
        return True
    else:
        return False
print(palindrom("шалаш"))


