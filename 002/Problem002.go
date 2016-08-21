package main

import (
    "fmt"
    "time"
)

func main() {
    var (
        sum uint64
        a   uint64
        b   uint64
    )

    start := time.Now()

    sum = 0
    a, b = 1, 1

    for b < 4000000 {
        if b%2 == 0 {
            sum += b
        }
        a, b = b, a+b
    }

    fmt.Printf("Sum: %d, took %s.\n", sum, time.Since(start))

}
