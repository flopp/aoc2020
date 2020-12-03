.PHONY: all
all:
	@echo "TARGETS: test1 part1 test2 part2 clean"

.PHONY: clean
clean:
	rm -f program1 program2

program1: program1.cpp
	g++ -std=c++11 -O2 -Wall -Wextra -o $@ $<

program2: program2.cpp
	g++ -std=c++11 -O2 -Wall -Wextra -o $@ $<

.PHONY: test1
test1: program1
	@echo "EXPECTED: 2"
	@./program1 < test.txt

.PHONY: part1
part1: program1
	@echo "EXPECTED: ?"
	@./program1 < data.txt

.PHONY: test2
test2: program2
	@echo "EXPECTED: 336"
	@./program2 < test.txt

.PHONY: part2
part2: program2
	@echo "EXPECTED: ?"
	@./program2 < data.txt
