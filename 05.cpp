#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

int get_seat_id(const std::string& s) {
    int id = 0;
    for (char c: s) {
        id = id * 2 + ((c == 'B' || c == 'R') ? 1 : 0);
    }
    return id;
}

int main() {
    int max_seat_id = -1;
    std::vector<bool> occupied(128 * 8, false);
    
    std::string line;
    while (std::getline(std::cin, line)) {
        int seat_id = get_seat_id(line);
        max_seat_id = std::max(max_seat_id, seat_id);
        occupied[seat_id] = true;
    }

    std::cout << "PART1" << std::endl;
    std::cout << max_seat_id << std::endl;
    
    int my_seat_id = -1;
    for (int id = 1; id < 128 * 8 - 1; ++id) {
        if (occupied[id - 1] && !occupied[id] && occupied[id + 1]) {
            my_seat_id = id;
            break;
        }
    }

    std::cout << "PART2" << std::endl;
    std::cout << my_seat_id << std::endl;

    return 0;
}
