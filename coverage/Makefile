CXX = g++

CFLAGS = -Werror -Wall -Wextra -fPIC -fprofile-arcs -ftest-coverage

TARGET = program

SOURCES = ../main.cpp

rebuild: clean build

build:
	$(CXX) $(CFLAGS) -o $(TARGET) $(SOURCES)

clean:
	rm -f $(TARGET)

run: build
	./program

report: run
	gcov $(SOURCES)
	# Create lcov report
	lcov --capture --directory . --output-file coverage.info
	#filter system-files
	lcov --remove coverage.info '/usr/*' --output-file coverage.info 
	# debug info
	lcov --list coverage.info
	# generating html output 
	genhtml coverage.info --output-directory out