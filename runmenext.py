class Solution:
   def solve(self, s):
      seen = s[0]
      ans = s[0]
      for i in s[1:]:
         if i != seen:
            ans += i
            seen = i
      return ans

ob = Solution()
s= open("pswdfile.txt","r")
f = s.read()
s.close()
test = ob.solve(str(f))

# Saved PIN: 3231   Center-Left-Center-Right

if test.startswith("3231"):
    print("Successfully Authenticated")
else:
    print("Failure in Authentication")