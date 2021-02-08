#include <iostream>

#include <vector>

int knapsack(std::vector<int>& vals, std::vector<int>& weights, int capacity) {

    std::vector<std::vector<int>> sack(weights.size() + 1, std::vector<int>(capacity + 1));

    // basically calculate every subset of items up to a given weight (capacity)
    for (int i = 0; i <= weights.size(); ++i) {

        for (int j = 0; j <= capacity; ++j) {
            
            if (i == 0 || j == 0) { //1st iteration start with 0
                sack[i][j] = 0;
            }
            else if (weights[i - 1] <= j) { //if we can take the item and we stay below weight
                sack[i][j] = std::max(vals[i - 1] + sack[i - 1][j - weights[i - 1]],
                    sack[i - 1][j]);
            }
            else { // else it would be too heavy, so carry old number forward
                sack[i][j] = sack[i - 1][j];
            }
        }
    }

    return sack[weights.size()][capacity];
}

int getMaxProfits(int savings, std::vector<int>& currVals, std::vector<int>& futureVals) {

    //we have weights, so we need values to complete knapsack
    std::vector<int> values(currVals.size());

    for (int i = 0; i < currVals.size(); ++i) {
        int actualVal = futureVals[i] - currVals[i];
        if (actualVal < 0) {
            actualVal = 0; //worst case would be 0, not negative
        }
        values[i] = actualVal;
    }

    // parameters are vals, weights, and capacity
    return knapsack(values, currVals, savings);
}


int main(void) {
    int savings = 250;
    std::vector<int> currVals = { 175, 133, 109, 201, 97};
    std::vector<int> futureVals = { 200, 125, 128, 228, 133};
    std::cout << getMaxProfits(savings, currVals, futureVals) << std::endl;

    return 0;
}
