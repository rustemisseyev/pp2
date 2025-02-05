def IsItPalindrome(num):
    global x, y
    x = 0
    y = -1
    for i in range(len(num) // 2):
            if num[x] == num[y]:
                  x += 1
                  y -= 1
            else:
                  return False
    return True
print(IsItPalindrome("madam"))
print(IsItPalindrome("saas"))
print(IsItPalindrome("saassasasasssss"))