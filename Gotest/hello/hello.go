package main

import (
	"fmt"

	"example.com/greetings"
)

func main() {
	// 获取问候消息并打印。
	message := greetings.Hello("Gladys")
	fmt.Println(message)
}
