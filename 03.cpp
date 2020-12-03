#include <iostream>
#include <string>
#include <vector>
#include "utilities/xy.h"

typedef XY<unsigned int> P;
typedef std::vector<std::string> Grid;

int check_slope(const Grid& grid, const P& slope) {
    int count = 0;
    for (P p{0, 0}; p.y < grid.size(); p += slope) {
        if (grid[p.y][p.x % grid[0].size()] == '#') {
            ++count;
        }
    }
    return count;
}

int main() {
    Grid grid;
    std::string line;
    while (std::getline(std::cin, line)) {
        grid.push_back(line);
    }

    std::cout << "PART1" << std::endl;
    std::cout << check_slope(grid, P{3,1}) << std::endl;

    std::cout << "PART2" << std::endl;
    unsigned long int result = 1;
    for (auto slope: {P{1,1}, P{3,1}, P{5,1}, P{7,1}, P{1,2}}) {
        result *= check_slope(grid, slope);
    }
    std::cout << result << std::endl;

    return 0;
}
