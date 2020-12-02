#include <iostream>
#include <unordered_set>

int main() {
    std::unordered_set<int> expenses;
    int expense;
    while (std::cin >> expense) {
        expenses.insert(expense);
    }

    for (auto value1: expenses) {
        const int rest = 2020 - value1;
        for (int value2 = 1; value2 < rest; ++value2) {
            const int value3 = rest - value2;
            if ((expenses.find(value2) != expenses.end()) &&
                (expenses.find(value3) != expenses.end()))
            {
                std::cout << (value1 * value2 * value3) << std::endl;
                return 0;
            }
        }
    }

    return 1;
}
