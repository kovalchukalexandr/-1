subsequence = [3, 4, 2, 5, 3, 5, 6, 7, 4]
i = 1
palindrome = ["No"]
while i < len(subsequence):
    k = 0
    dum = True
    while k < i:
        if subsequence[k] == subsequence[i]:
            palindrome.append("Yes")
            dum = False
        k += 1
    if dum != False:
        palindrome.append("No")
    i += 1
print(palindrome)