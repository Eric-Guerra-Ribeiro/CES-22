def is_palindrome(strg):
    """
    Returns True if string strg is palindrome, False otherwise.
    """
    str_len = len(strg)
    for i in range(str_len//2):
        if strg[i] != strg[str_len - 1 - i]:
            return False
    return True


assert is_palindrome("a") == True
assert is_palindrome("ab") == False
assert is_palindrome("aa") == True
assert is_palindrome("arara") == True
assert is_palindrome("") == True
assert is_palindrome("ababacbaba") == False
assert is_palindrome("racecar") == True
assert is_palindrome("pickles") == False
assert is_palindrome("saippuakivikauppias") == True
assert is_palindrome("Sit on a potato pan, Otis.") == False
assert is_palindrome("sitonapotatopanotis") == True
