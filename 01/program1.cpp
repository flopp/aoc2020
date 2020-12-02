#include <iostream>
#include <unordered_set>

int main() {
    std::unordered_set<int> expenses;
    int expense1;
    while (std::cin >> expense1) {
        const int expense2 =  2020 - expense1;
        if (expenses.find(expense2) != expenses.end()) {
            std::cout << (expense1 * expense2) << std::endl;
            return 0;
        }
        expenses.insert(expense1);
    }
    return 1;
}
