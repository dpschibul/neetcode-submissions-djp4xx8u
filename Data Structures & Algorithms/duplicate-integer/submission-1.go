func hasDuplicate(nums []int) bool {
    seen := make(map[int]struct{})

    for _, i := range nums {
        if _, exists := seen[i]; exists {
            return true
        }
        seen[i] = struct{}{}
    }


    return false
}
