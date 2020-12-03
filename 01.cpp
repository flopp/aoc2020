#include <iostream>
#include <unordered_set>

typedef std::unordered_set<int> Expenses;

int part1(const Expenses& expenses) {
    for (auto value1: expenses) {
        const int value2 = 2020 - value1;
        if ((expenses.find(value2) != expenses.end())) {
            return value1 * value2;
        }
    }
    return -1;
}

int part2(const Expenses& expenses) {
    for (auto value1: expenses) {
        const int rest = 2020 - value1;
        for (int value2 = 1; value2 < rest; ++value2) {
            const int value3 = rest - value2;
            if ((expenses.find(value2) != expenses.end()) &&
                (expenses.find(value3) != expenses.end()))
            {
                return value1 * value2 * value3;
            }
        }
    }
    return -1;
}

int main() {
    Expenses expenses;
    int expense;
    while (std::cin >> expense) {
        expenses.insert(expense);
    }

    std::cout << "PART1" << std::endl;
    std::cout << part1(expenses) << std::endl;

    std::cout << "PART2" << std::endl;
    std::cout << part2(expenses) << std::endl;

    return 0;
}
