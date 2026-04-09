class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if (s.length != t.length) {
            return false;
        }
        const s_arr = Array(26).fill(0);
        const t_arr = Array(26).fill(0);
        for(const i in s) {
            const sCharCode = s.charCodeAt(i) - 'a'.charCodeAt(0);
            const tCharCode = t.charCodeAt(i) - 'a'.charCodeAt(0);
            s_arr[sCharCode]++;
            t_arr[tCharCode]++;
        }

        for(const i in s_arr)  {
            if (s_arr[i] !== t_arr[i]) {
                return false;
            }
        }
        return true;
    }
}
