#include <iostream>
#include <vector>

int getMaxProfit(std::vector<int>* stocksPrices){
    int min_profit = 0;
    int max_profit = stocksPrices[1] - stocksPrices[0];
    return max_profit;
}

int main() {
    std::vector<int> stocksPrices = {4,2,6,9,0,1,10};
    std::cout << "Size " << stocksPrices.size() << std::endl;
    int max_profit = getMaxProfit(&stocksPrices);
    std::cout << "Max profit: " << max_profit << std::endl;
}
