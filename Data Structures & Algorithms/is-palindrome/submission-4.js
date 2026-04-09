class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        let left = 0;
        let right = s.length -1 ;

        while(left < right) {
            while(left < right && !isLetter(s.charAt(left))) {
                left += 1;
            }
            while(left < right && !isLetter(s.charAt(right))) {
                right -= 1;
            }

            if (s.charAt(left).toLowerCase() != s.charAt(right).toLowerCase()) {
                return false;
            }

            left += 1;
            right -= 1;
        }

        return true;
    }
}


function isLetter(char) {
    return /^[a-zA-Z0-9]$/.test(char);
}