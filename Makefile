.PHONY: all
all:
	@echo "Run day 01 with 'make 01-cpp', etc."

01-cpp: .build/01.cpp.bin
	$< < 01-test.txt
	$< < 01-data.txt

02-cpp: .build/02.cpp.bin
	$< < 02-test.txt
	$< < 02-data.txt

03-cpp: .build/03.cpp.bin
	$< < 03-test.txt
	$< < 03-data.txt

04-cpp: .build/04.cpp.bin
	$< < 04-test.txt
	$< < 04-data.txt



01-py:
	python3 01.py < 01-test.txt
	python3 01.py < 01-data.txt


.build/%.cpp.bin: %.cpp
	@mkdir -p .build
	g++ -std=c++11 -O2 -Wall -Wextra -o $@ $<
