#include <iostream>
#include <string>
#include <vector>

int main() {
    int max_seat_id = -1;
    std::vector<bool> occupied(128 * 8, false);
    
    std::string line;
    while (std::getline(std::cin, line)) {
        int row = 0;
        int column = 0;
        Seat seat;
        for (char c: line) {
            switch (c) {
                case 'F':
                    row = 2 * row;
                    break;
                case 'B':
                    row = 2 * row + 1;
                    break;
                case 'L':
                    column = 2 * column;
                    break;
                case 'R':
                    column = 2 * column + 1;
                    break;
            }
        }
        int seat_id = row * 8 + column;
        if (seat_id > max_seat_id) {
            max_seat_id = seat_id;
        }
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
