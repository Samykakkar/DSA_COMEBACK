func isPalindrome(x int) bool {
    
   str:=strconv.Itoa(x)
   for first, second :=0,len(str)-1; first<=second; first,second=first+1,second-1{
    if str[first]!=str[second]{
        return false}
   }
   return true
}