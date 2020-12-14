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

05-cpp: .build/05.cpp.bin
	$< < 05-test.txt
	$< < 05-data.txt


01-py:
	python3 01.py < 01-test.txt
	python3 01.py < 01-data.txt

04-py:
	python3 04.py < 04-test.txt
	python3 04.py < 04-data.txt

05-py:
	python3 05.py < 05-test.txt
	python3 05.py < 05-data.txt

06-py:
	python3 06.py < 06-test.txt
	python3 06.py < 06-data.txt

07-py:
	python3 07.py < 07-test.txt
	python3 07.py < 07-data.txt

08-py:
	python3 08.py < 08-test.txt
	python3 08.py < 08-data.txt

09-py:
	python3 09.py 5 < 09-test.txt
	python3 09.py 25 < 09-data.txt

10-py:
	python3 10.py < 10-test.txt
	python3 10.py < 10-data.txt

11-py:
	python3 11.py < 11-test.txt
	python3 11.py < 11-data.txt

12-py:
	python3 12.py < 12-test.txt
	python3 12.py < 12-data.txt

13-py:
	python3 13.py < 13-test.txt
	python3 13.py < 13-data.txt

14-py:
	#python3 14.py < 14-test.txt
	python3 14.py < 14-test2.txt
	python3 14.py < 14-data.txt

.build/%.cpp.bin: %.cpp
	@mkdir -p .build
	g++ -std=c++11 -O2 -Wall -Wextra -o $@ $<
