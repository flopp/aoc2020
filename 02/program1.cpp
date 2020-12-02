#include <iostream>
#include <regex>
#include <string>

bool is_valid_password(
    const std::string& password,
    int policy_min,
    int policy_max,
    char policy_letter
) {
    int count = 0;
    for (auto c: password) {
        if (c == policy_letter) {
            ++count;
        }
    }
    return ((policy_min <= count) && (count <= policy_max));
}

int main() {
    const std::regex re{"^\\s*(\\d+)-(\\d+) ([a-z]): ([a-z]+)\\s*$"};

    int valid_passwords = 0;
    std::string line;
    while (std::getline(std::cin, line)) {
        std::smatch match;
        if (std::regex_match(line, match, re)) {
            if (is_valid_password(match[4], std::stoi(match[1]), std::stoi(match[2]), *(match[3].first))) {
                ++valid_passwords;
            }
        }
    }
    std::cout << valid_passwords << std::endl;
    return 0;
}
