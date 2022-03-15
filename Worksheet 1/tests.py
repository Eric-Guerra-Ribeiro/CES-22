import problem1
import problem2
import problem3
import problem4
import problem5

# Problem 1
print("Problem 1:")
problem1.main()
print("Passed problem 1.")

# Problem 2
print("Problem 2:")
problem2.main()
print("Passed problem 2.")

# Problem 3
print("Problem 3:")
for i in range (100):
    assert problem3.sum_to(i) == problem3.sum_to_gauss(i)
print("Passed problem 3.")

# Problem 4
print("Problem 4:")
assert problem4.is_prime(0) == False
assert problem4.is_prime(1) == False
assert problem4.is_prime(2) == True
assert problem4.is_prime(3) == True
assert problem4.is_prime(4) == False
assert problem4.is_prime(5) == True
assert problem4.is_prime(6) == False
assert problem4.is_prime(7) == True
assert problem4.is_prime(8) == False
assert problem4.is_prime(9) == False
assert problem4.is_prime(9941) == True
assert problem4.is_prime(9943) == False
assert problem4.is_prime(-1) == False
assert problem4.is_prime(-2) == True
assert problem4.is_prime(-3) == True
assert problem4.is_prime(-4) == False
assert problem4.is_prime(-5) == True
assert problem4.is_prime(-6) == False
assert problem4.is_prime(-7) == True
assert problem4.is_prime(-8) == False
assert problem4.is_prime(-9) == False
assert problem4.is_prime(-9941) == True
assert problem4.is_prime(-9943) == False
print("Passed problem 4.")

# Problem 5
print("Problem 5:")
assert problem5.is_palindrome("") == True
assert problem5.is_palindrome("a") == True
assert problem5.is_palindrome("ab") == False
assert problem5.is_palindrome("aa") == True
assert problem5.is_palindrome("arara") == True
assert problem5.is_palindrome("ababacbaba") == False
assert problem5.is_palindrome("racecar") == True
assert problem5.is_palindrome("pickles") == False
assert problem5.is_palindrome("saippuakivikauppias") == True
assert problem5.is_palindrome("Sit on a potato pan, Otis.") == False
assert problem5.is_palindrome("sitonapotatopanotis") == True
print("Passed problem 5.")
