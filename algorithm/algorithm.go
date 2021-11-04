package main

import (
	"fmt"
	"math"
)

func square() {
	var y = float32(64)
	fmt.Println("内置函数平方根：", math.Sqrt(float64(y)))
	var x = y
	for (x*x - y) > 0.0001 { // 浮点数位数越多精度越准
		x = (x + y/x) / 2
	}
	fmt.Println("牛顿求平方根：", x)

	x2 := y
	i := math.Float32bits(y)
	i = 0x5f3759df - (i >> 1)
	x2 = math.Float32frombits(i)
	for a := 0; a < 3; a++ { // 循环次数越多 精度越准
		x2 = x2 * (1.5 - (0.5 * y * x2 * x2))
	}
	fmt.Println("雷神之锤3源码求平方根", 1/x2)
}

func main() {

}
