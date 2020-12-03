#include <iostream>
#include <string>
#include "../utilities/xy.h"

int check_slope(
    const std::string& grid,
    const XY<unsigned int>& size,
    const XY<unsigned int>& slope
) {
    int count = 0;
    for (XY<unsigned int> pos{0, 0}; pos.y < size.y; pos += slope) {
        if (grid[(pos.y * size.x) +  (pos.x % size.x)] == '#') {
            ++count;
        }
    }
    return count;
}

int main() {
    XY<unsigned int> size;
    std::string grid;
    std::string line;
    while (std::getline(std::cin, line)) {
        size.x = line.size();
        grid += line;
    }
    size.y = grid.size() / size.x;

    unsigned long int result = 1;
    for (auto slope: {XY<unsigned int>{1,1}, XY<unsigned int>{3,1}, XY<unsigned int>{5,1}, XY<unsigned int>{7,1}, XY<unsigned int>{1,2}}) {
        result *= check_slope(grid, size, slope);
    }
    std::cout << result << std::endl;

    return 0;
}
