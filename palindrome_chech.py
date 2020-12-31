def Palindrome(n, odd): 
  
    result = n; 
    if (odd): 
        n = int(n / 10); 
    while (n > 0): 
        result = 10 * result + n % 10; 
        n = int(n / 10); 
    return result; 
  
def isPalindrome(n, base): 
    reversed = 0; 
    temp = n; 
    while (temp > 0):  
        reversed = reversed * base + temp % base; 
        temp = int(temp / base); 
      
    return reversed == n; 
  
  
def sumPalindrome(n, k):  
  
    sum = 0;  
    i = 1; 
  
    p = Palindrome(i, True); 
  
    while (p < n): 
        if (isPalindrome(p, k)): 
            sum += p; 
        i += 1; 
  
        p = Palindrome(i, True); 
  
    i = 1; 
  
    p = Palindrome(i, False); 
    while (p < n): 
        if (isPalindrome(p, k)): 
            sum += p; 
        i += 1; 
        p = Palindrome(i, False); 
  
    print("Total sum is", sum); 
  
n = 1000000;  
k = 2; 
sumPalindrome(n, k);
def Palindrome(n, odd): 
  
    result = n; 
    if (odd): 
        n = int(n / 10); 
    while (n > 0): 
        result = 10 * result + n % 10; 
        n = int(n / 10); 
    return result; 
  
def isPalindrome(n, base): 
    reversed = 0; 
    temp = n; 
    while (temp > 0):  
        reversed = reversed * base + temp % base; 
        temp = int(temp / base); 
      
    return reversed == n; 
  
def sumPalindrome(n, k):  
  
    sum = 0;  
    i = 1; 
  
    p = Palindrome(i, True); 
  
    while (p < n): 
        if (isPalindrome(p, k)): 
            sum += p; 
        i += 1; 
  
        p = Palindrome(i, True); 
  
    i = 1; 
  
    p = Palindrome(i, False); 
    while (p < n): 
        if (isPalindrome(p, k)): 
            sum += p; 
        i += 1; 
        p = Palindrome(i, False); 
  
    print("Total sum is", sum); 
  
n = 1000000;  
k = 2; 
sumPalindrome(n, k);