// https://leetcode.com/problems/range-sum-query-2d-immutable/

package main

type NumMatrix struct {
    sumMatrix [][]int
}


func Constructor(matrix [][]int) NumMatrix {
    sums := [][]int{}

    // loop by row
    for _, row := range matrix { 
        rowSums := []int{}

        // loop by column
        for colIndex, num := range row {
            if colIndex == 0 {
                rowSums = append(rowSums, num)
                continue
            }
            rowSums = append(rowSums, rowSums[colIndex-1] + num)
        }

        fmt.Println(rowSums)
        sums = append(sums, rowSums)

    }

    return NumMatrix{
        sumMatrix: sums,
    }
}


func (this *NumMatrix) SumRegion(row1 int, col1 int, row2 int, col2 int) int {
    sums := 0
    
    for row:=row1; row<=row2; row++ {
        if col1 > 0 {
            // get the number outside left square area to minus
            sums += this.sumMatrix[row][col2] - this.sumMatrix[row][col1-1]
        } else {
             sums += this.sumMatrix[row][col2]
        }
    }

    return sums
}


/**
 * Your NumMatrix object will be instantiated and called as such:
 * obj := Constructor(matrix);
 * param_1 := obj.SumRegion(row1,col1,row2,col2);
 */