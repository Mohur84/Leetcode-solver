class Solution:
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        if indexDiff <= 0 or valueDiff < 0:
            return False
        buckets = {}
        size = valueDiff + 1
        def bucket_id(x):
            return x // size
        for i, x in enumerate(nums):
            b = bucket_id(x)
            if b in buckets:
                return True
            if b - 1 in buckets:
                if abs(x - buckets[b - 1]) <= valueDiff:
                    return True
            if b + 1 in buckets:
                if abs(x - buckets[b + 1]) <= valueDiff:
                    return True
            buckets[b] = x
            if i >= indexDiff:
                old = nums[i - indexDiff]
                old_bucket = bucket_id(old)
                del buckets[old_bucket]
        return False