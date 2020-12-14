package main

func findMaxAverage(nums []int, k int) float64 {
	sum := 0
	// sum up to first k
	for i := 0; i < k; i++ {
		sum += nums[i]
	}

	max := sum
	pointer := k

	for pointer < len(nums) {
		sum = sum - nums[pointer-k] + nums[pointer]
		if sum > max {
			max = sum
		}
		pointer++
	}

	return float64(max) / float64(k)
}
