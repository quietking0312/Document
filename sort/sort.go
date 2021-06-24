package main

import (
	"fmt"
	"io/ioutil"
	"math"
	"os"
	"path"
	"strconv"
	"strings"
	"time"
)

func getData() []int {
	var arr []int
	f, err := os.OpenFile(path.Join("data.text"), os.O_RDONLY, 0600)
	defer f.Close()
	if err != nil {
		fmt.Println(err)
	} else {
		data, err := ioutil.ReadAll(f)
		if err != nil {
			return nil
		}
		dataStr := string(data)
		arrStr := strings.Split(dataStr, ",")
		for _, s := range arrStr {
			a, _ := strconv.Atoi(s)
			arr = append(arr, a)
		}
		return arr
	}
	return nil
}

func saveData(arr []int) {
	var arrStr []string
	for _, s := range arr {
		arrStr = append(arrStr, strconv.FormatInt(int64(s), 10))
	}
	data := strings.Join(arrStr, ",")
	_ = ioutil.WriteFile("out.text", []byte(data), 0666)
}

// 冒泡排序
func bubbleSort(arr []int) []int {
	length := len(arr)
	for i := 0; i < length; i++ {
		for j := 0; j < length-1-i; j++ {
			if arr[j] > arr[j+1] {
				arr[j], arr[j+1] = arr[j+1], arr[j]
			}
		}
	}
	return arr
}

// 选择排序
func selectionSort(arr []int) []int {
	length := len(arr)
	for i := 0; i < length-1; i++ {
		min := i
		for j := i + 1; j < length; j++ {
			if arr[min] > arr[j] {
				min = j
			}
		}
		arr[i], arr[min] = arr[min], arr[i]
	}
	return arr
}

// 插入排序
func insertionSort(arr []int) []int {
	for i := range arr {
		preIndex := i - 1
		current := arr[i]
		for preIndex >= 0 && arr[preIndex] > current {
			arr[preIndex+1] = arr[preIndex]
			preIndex -= 1
		}
		arr[preIndex+1] = current
	}
	return arr
}

// 希尔排序
func shellSort(arr []int) []int {
	length := len(arr)
	gap := 1
	for gap < gap/3 {
		gap = gap*3 + 1
	}
	for gap > 0 {
		for i := gap; i < length; i++ {
			temp := arr[i]
			j := i - gap
			for j > 0 && arr[j] > temp {
				arr[j+gap] = arr[j]
				j -= gap
			}
			arr[j+gap] = temp
		}
		gap = gap / 3
	}
	return arr
}

// 归并排序
func mergeSort(arr []int) []int {
	length := len(arr)
	if length < 2 {
		return arr
	}
	middle := length / 2
	left := arr[0:middle]
	right := arr[middle:]
	return merge(mergeSort(left), mergeSort(right))
}

func merge(left []int, right []int) []int {
	var result []int
	for len(left) != 0 && len(right) != 0 {
		if left[0] <= right[0] {
			result = append(result, left[0])
			left = left[1:]
		} else {
			result = append(result, right[0])
			right = right[1:]
		}
	}
	for len(left) != 0 {
		result = append(result, left[0])
		left = left[1:]
	}
	for len(right) != 0 {
		result = append(result, right[0])
		right = right[1:]
	}
	return result
}

// 快速排序
func quickSort(arr []int) []int {
	return _quickSort(arr, 0, len(arr)-1)
}

func _quickSort(arr []int, left, right int) []int {
	if left < right {
		partitionIndex := partition(arr, left, right)
		_quickSort(arr, left, partitionIndex-1)
		_quickSort(arr, partitionIndex+1, right)
	}
	return arr
}

func partition(arr []int, left, right int) int {
	pivot := left
	index := pivot + 1
	for i := index; i <= right; i++ {
		if arr[i] < arr[pivot] {
			swap(arr, i, index)
			index += 1
		}
	}
	swap(arr, pivot, index-1)
	return index - 1
}

func swap(arr []int, i, j int) {
	arr[i], arr[j] = arr[j], arr[i]
}

// 堆排序
func heapSort(arr []int) []int {
	arrLen := len(arr)
	buildMaxHeap(arr, arrLen)
	for i := arrLen - 1; i >= 0; i-- {
		swap(arr, 0, i)
		arrLen -= 1
		heapify(arr, 0, arrLen)
	}
	return arr
}

func buildMaxHeap(arr []int, arrLen int) {
	for i := arrLen / 2; i >= 0; i-- {
		heapify(arr, i, arrLen)
	}
}

func heapify(arr []int, i, arrLen int) {
	left := 2*i + 1
	right := 2*i + 2
	largest := i
	if left < arrLen && arr[left] > arr[largest] {
		largest = left
	}
	if right < arrLen && arr[right] > arr[largest] {
		largest = right
	}
	if largest != i {
		swap(arr, i, largest)
		heapify(arr, largest, arrLen)
	}
}

// 计数排序
func countingSort(arr []int, maxValue int) []int {
	backetLen := maxValue + 1
	backet := make([]int, backetLen)
	sortedIndex := 0
	length := len(arr)
	for i := 0; i < length; i++ {
		backet[arr[i]] += 1
	}
	for j := 0; j < backetLen; j++ {
		for backet[j] > 0 {
			arr[sortedIndex] = j
			sortedIndex += 1
			backet[j] -= 1
		}
	}
	return arr
}

// 桶排序
func bucketSort(arr []int, bucketSize int) []int {
	minValue := arr[0]
	maxValue := arr[0]
	for i := 1; i < len(arr); i++ {
		if arr[i] < minValue {
			minValue = arr[i]
		} else if arr[i] > maxValue {
			maxValue = arr[i]
		}
	}
	bucketCount := math.Floor(float64((maxValue-minValue)/bucketSize)) + 1
	buckets := make([][]int, int(bucketCount))
	for i := 0; i < len(buckets); i++ {
		buckets[i] = []int{}
	}
	for i := 0; i < len(arr); i++ {
		index := int(math.Floor(float64((arr[i] - minValue) / bucketSize)))
		buckets[index] = append(buckets[index], arr[i])
	}
	arr = []int{}
	for i := 0; i < len(buckets); i++ {
		insertionSort(buckets[i])
		for j := 0; j < len(buckets[i]); j++ {
			arr = append(arr, buckets[i][j])
		}
	}
	return arr
}

func main() {
	arr := getData()
	startTime := time.Now()
	// bubbleSort(arr)
	// mergeSort(arr)
	// quickSort(arr)
	// countingSort(arr, len(arr))
	bucketSort(arr, 5)
	// heapSort(arr)
	// selectionSort(arr)
	subTime := time.Now().Sub(startTime)
	fmt.Printf("时间差： %f\n", subTime.Seconds())
}
