#include <fstream>
#include <string>
#include <iostream>
#include <vector>
#include <queue>
#include <map>
#include <unordered_map>
#include <set>
#include <algorithm>

struct File
{
    std::string name;
    int size;
};

struct Dir
{
    std::string name;
    std::vector<Dir> dirs;
    std::vector<File> files;
};

template<typename T> std::vector<T> split(const T & input, const T & delimiters)
{
    std::vector<T> temporary;
    size_t start = 0;

    auto pos = input.find_first_of(delimiters, start);
    while(pos != T::npos) {
        if(pos != start) // ignore empty tokens
        {
            temporary.emplace_back(
                    input,
                    start,
                    pos - start
            );
        }
        start = pos + 1;
        pos = input.find_first_of(delimiters, start);
    }

    if(start < input.length()) // ignore trailing delimiter
    {
        temporary.emplace_back(
                input,
                start,
                input.length() - start
        );
    }
    return temporary;
}

std::ifstream infile("../../05/input.txt");
std::string ReadFile()
{
//    std::string lines;
    std::string line;
    Dir dir;
    if (infile.is_open())
    {
        while ( getline (infile,line) )
        {
            const auto& terminalOutput = split<std::string>(line, " ");
            for(const auto& out : terminalOutput)
            {
                if("$")
                {
                    if()
                    {

                    }
                }
                if("dir")
                {
                }
            }
        }
        infile.close();
    }

    return line;
}

void pt1()
{

}

void pt2()
{

}

int main()
{
    p1();
    p2();
}