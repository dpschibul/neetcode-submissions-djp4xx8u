class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        const map = new Map();

        for (const str of strs) {
            const charArray = new Array(26).fill(0);

            for (const c of str) {
                charArray[c.charCodeAt(0)-'a'.charCodeAt(0)]++;
            }
            if (map.has(charArray.toString())) {
                map.get(charArray.toString()).push(str)
            } else {
                map.set(charArray.toString(), [str])
            }
        }

        let res = [];

        map.forEach((value, key) => {
            let cur = [];

            for(const val of value) {
                cur.push(val);
            }
            res.push(cur);
        })
        return res;

    }
}
