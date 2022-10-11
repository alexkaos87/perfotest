CXX = g++

CFLAGS = -Werror -Wall -Wextra

TARGET = program

SOURCES = main.cpp

rebuild: clean build

build:
	$(CXX) $(CFLAGS) -o $(TARGET) $(SOURCES)

clean:
	rm -f $(TARGET)

run: build
	./program