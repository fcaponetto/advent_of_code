#include <fstream>
#include <string>
#include <iostream>
#include <vector>
#include <queue>

std::vector<std::string> ReadFile()
{
    std::ifstream infile("../01/input.txt");

    std::vector<std::string> lines;
    std::string line;
    if (infile.is_open())
    {
        while ( getline (infile,line) )
        {
            lines.push_back(line);
        }
        infile.close();
    }

    return lines;
}


void pt1()
{
    const auto lines = ReadFile();

    int maxCalories = 0, tmpCalories = 0;
    for(const auto& line : lines)
    {
        if(line == "")
        {
            if(tmpCalories > maxCalories)
            {
                maxCalories = tmpCalories;
            }
            tmpCalories = 0;
        }
        tmpCalories+= atoi(line.c_str());
    }

    std::cout << maxCalories;
};

void pt2()
{
    const auto lines = ReadFile();
    std::priority_queue<int, std::vector<int>, std::greater<int>> data;

    int tmpCalories = 0;
    for(const auto& line : lines)
    {
        if(line == "")
        {
            data.push(tmpCalories);
            if (data.size() > 3)
            {
                data.pop();
            }
            tmpCalories = 0;
        }

        tmpCalories+= atoi(line.c_str());
    }

    int totTopThree = 0;
    for(;!data.empty(); data.pop())
    {
       totTopThree += data.top();
        std::cout << data.top() << " ";
    }

    std::cout << totTopThree <<  std::endl;
}

int main()
{
    pt2();
}