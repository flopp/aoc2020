.PHONY: all
all:
	@echo "Run day 01 with 'make 01-cpp', etc."

.PHONY: setup
setup:
	python3 -m venv .env
	.env/bin/pip install --upgrade pip
	.env/bin/pip install --upgrade regex

.build/%.cpp.bin: %.cpp
	@mkdir -p .build
	g++ -std=c++11 -O2 -Wall -Wextra -o $@ $<

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
	.env/bin/python 01.py < 01-test.txt
	.env/bin/python 01.py < 01-data.txt

04-py:
	.env/bin/python 04.py < 04-test.txt
	.env/bin/python 04.py < 04-data.txt

05-py:
	.env/bin/python 05.py < 05-test.txt
	.env/bin/python 05.py < 05-data.txt

06-py:
	.env/bin/python 06.py < 06-test.txt
	.env/bin/python 06.py < 06-data.txt

07-py:
	.env/bin/python 07.py < 07-test.txt
	.env/bin/python 07.py < 07-data.txt

08-py:
	.env/bin/python 08.py < 08-test.txt
	.env/bin/python 08.py < 08-data.txt

09-py:
	.env/bin/python 09.py 5 < 09-test.txt
	.env/bin/python 09.py 25 < 09-data.txt

10-py:
	.env/bin/python 10.py < 10-test.txt
	.env/bin/python 10.py < 10-data.txt

11-py:
	.env/bin/python 11.py < 11-test.txt
	.env/bin/python 11.py < 11-data.txt

12-py:
	.env/bin/python 12.py < 12-test.txt
	.env/bin/python 12.py < 12-data.txt

13-py:
	.env/bin/python 13.py < 13-test.txt
	.env/bin/python 13.py < 13-data.txt

14-py:
	#.env/bin/python 14.py < 14-test.txt
	.env/bin/python 14.py < 14-test2.txt
	.env/bin/python 14.py < 14-data.txt

15-py:
	.env/bin/python 15.py < 15-test.txt
	.env/bin/python 15.py < 15-data.txt

16-py:
	#.env/bin/python 16.py < 16-test.txt
	.env/bin/python 16.py < 16-data.txt

17-py:
	.env/bin/python 17.py < 17-test.txt
	.env/bin/python 17.py < 17-data.txt

18-py:
	.env/bin/python 18.py < 18-test.txt
	.env/bin/python 18.py < 18-data.txt

19-py:
	.env/bin/python 19.py < 19-test.txt
	.env/bin/python 19.py < 19-test2.txt
	.env/bin/python 19.py < 19-data.txt
