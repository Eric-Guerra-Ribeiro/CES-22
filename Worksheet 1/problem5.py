def is_palindrome(strg):
    """
    Returns True if string strg is palindrome, False otherwise.
    """
    str_len = len(strg)
    for i in range(str_len//2):
        if strg[i] != strg[str_len - 1 - i]:
            return False
    return True
