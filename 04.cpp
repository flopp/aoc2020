#include <iostream>
#include <map>
#include <regex>
#include <set>
#include <string>
#include <vector>

typedef std::map<std::string, std::string> Fields;


std::vector<Fields> parse(std::istream& is) {
    static const std::regex re{"(...):(\\S+)"};

    std::vector<Fields> records;
    Fields fields;

    std::string line;
    while (std::getline(is, line)) {
        if (line.empty() && !fields.empty()) {
            records.push_back(fields);
            fields.clear();
        }
        auto begin = std::sregex_iterator(line.begin(), line.end(), re);
        auto end = std::sregex_iterator();
        for (std::sregex_iterator i = begin; i != end; ++i) {
            std::smatch match = *i;
            fields[match[1].str()] = match[2].str();
        }
    }
    if (!fields.empty()) {
        records.push_back(fields);
    }

    return records;
}


bool is_valid_part1(const Fields& fields) {
    static const std::vector<std::string> keys{"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"};

    for (auto key: keys) {
        if (fields.find(key) == fields.end()) {
            return false;
        }
    }

    return true;
}


bool validate_int_range(const std::string& s, int min, int max) {
    static const std::regex re{"^\\d+$"};
    
    if (!std::regex_match(s, re)) {
        return false;
    }

    const int v = std::stoi(s);
    return min <= v && v <= max;
}


bool validate_byr(const std::string& s) {
    return validate_int_range(s, 1920, 2002);
}


bool validate_iyr(const std::string& s) {
    return validate_int_range(s, 2010, 2020);
}


bool validate_eyr(const std::string& s) {
    return validate_int_range(s, 2020, 2030);
}


bool validate_hgt(const std::string& s) {
    static const std::regex re_in{"^(\\d+)in$"};
    static const std::regex re_cm{"^(\\d+)cm$"};
    
    std::smatch match;
    if (std::regex_match(s, match, re_in)) {
        return validate_int_range(match[1].str(), 50, 76);
    } else if (std::regex_match(s, match, re_cm)) {
        return validate_int_range(match[1].str(), 150, 193);
    }

    return false;
}


bool validate_hcl(const std::string& s) {
    static const std::regex re{"^#[0-9a-f]{6}$"};
    return std::regex_match(s, re);
}


bool validate_ecl(const std::string& s) {
    static const std::set<std::string> colors{"amb", "blu", "brn", "gry", "grn", "hzl", "oth"};
    return colors.find(s) != colors.end();
}


bool validate_pid(const std::string& s) {
    static const std::regex re{"^[0-9]{9}$"};
    return std::regex_match(s, re);
}


bool is_valid_part2(const Fields& fields) {
    static std::map<std::string, std::function<bool(const std::string&)>> required = {
        {"byr", validate_byr},
        {"iyr", validate_iyr},
        {"eyr", validate_eyr},
        {"hgt", validate_hgt},
        {"hcl", validate_hcl},
        {"ecl", validate_ecl},
        {"pid", validate_pid},
    };
    
    for (auto validator: required) {
        auto it = fields.find(validator.first);
        if (it == fields.end()) {
            return false;
        }

        if (!validator.second(it->second)) {
            return false;
        }
    }
    
    return true;
}


int main() {
    const std::vector<Fields> records = parse(std::cin);
    
    int count_part1 = 0;
    int count_part2 = 0;

    for (auto fields: records) {
        if (is_valid_part1(fields)) {
            ++count_part1;
        }
        if (is_valid_part2(fields)) {
            ++count_part2;
        }
    }

    std::cout << "PART1" << std::endl;
    std::cout << count_part1 << std::endl;
    
    std::cout << "PART2" << std::endl;
    std::cout << count_part2 << std::endl;

    return 0;
}
