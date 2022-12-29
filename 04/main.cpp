#include <fstream>
#include <string>
#include <iostream>
#include <vector>
#include <queue>
#include <map>
#include <stack>

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

struct Instruction
{
    int num;
    int source;
    int dest;
};

std::vector<std::deque<char>> stacks;

std::vector<Instruction> ReadFile()
{
    std::ifstream infile("../../04/input.txt");

    std::string line;
    while(std::getline(infile, line))
    {
        if(line[1] == '1')
        {
            break;
        }
        for(int i = 0; i < stacks.size(); i++)
        {
            if(line[1 + (4*i)] == '\0' || line[1 + (4*i)] == ' ')
            {
                continue;
            }
            stacks[i].push_back(line[1+(4*i)]);
        }
    }

    std::vector<std::string> temp;
    std::vector<Instruction> movements;
    Instruction instruction;

    std::getline(infile, line);
    while(std::getline(infile, line)) {
        temp = split<std::string>(line, " ");
        instruction.num = atoi(temp[1].c_str());
        instruction.source = atoi(temp[3].c_str()) - 1;
        instruction.dest = atoi(temp[5].c_str()) - 1;

        movements.push_back(instruction);
    }
    infile.close();

    return movements;
}

//void pt1()
//{
//    const auto movements = ReadFile();
//
//    for (const auto& instruction : movements)
//    {
//        for(int i = 0; i < instruction.num; i++)
//        {
//            stacks[instruction.dest].push_front(stacks[instruction.source].front());
//            stacks[instruction.source].pop_front();
//        }
//    }
//
//    for(const auto& stack : stacks)
//    {
//        std::cout << stack.front();
//    }
//    std::cout << std::endl;
//}

void pt2()
{
    const auto movements = ReadFile();

    std::deque<char> tmp;
    for (const auto& instruction : movements)
    {
        for(int i = 0; i < instruction.num; i++)
        {
            tmp.push_front(stacks[instruction.source].front());
            stacks[instruction.source].pop_front();
        }

        for(int i = 0; i < instruction.num; i++)
        {
            stacks[instruction.dest].push_front(tmp.front());
            tmp.pop_front();
        }
    }

    for(const auto& stack : stacks)
    {
        std::cout << stack.front();
    }
    std::cout << std::endl;
}


int main()
{
//    stacks.resize(3);
//    pt1();
    stacks.resize(9);
    pt2();
}