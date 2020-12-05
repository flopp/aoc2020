#include <algorithm>
#include <iostream>
#include <regex>
#include <string>

bool is_valid_password_part1(
    const std::string& password, int min, int max, char letter
) {
    const int count = std::count(password.begin(), password.end(), letter);
    return ((min <= count) && (count <= max));
}

bool is_valid_password_part2(
    const std::string& password, int min, int max, char letter
) {
    return (password[min - 1] == letter) != (password[max - 1] == letter);
}

int main() {
    const std::regex re{"^\\s*(\\d+)-(\\d+) ([a-z]): ([a-z]+)\\s*$"};

    int valid_passwords_part1 = 0;
    int valid_passwords_part2 = 0;

    std::string line;
    while (std::getline(std::cin, line)) {
        std::smatch match;
        if (std::regex_match(line, match, re)) {
            const int min = std::stoi(match[1]);
            const int max = std::stoi(match[2]);
            const char letter = *(match[3].first);
            const std::string password = match[4];
        
            if (is_valid_password_part1(password, min, max, letter)) {
                ++valid_passwords_part1;
            }
            if (is_valid_password_part2(password, min, max, letter)) {
                ++valid_passwords_part2;
            }
        }
    }

    std::cout << "PART1" << std::endl;
    std::cout << valid_passwords_part1 << std::endl;

    std::cout << "PART2" << std::endl;
    std::cout << valid_passwords_part2 << std::endl;
    
    return 0;
}
