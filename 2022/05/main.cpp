#include <fstream>
#include <string>
#include <iostream>
#include <vector>
#include <queue>
#include <map>
#include <unordered_map>
#include <set>
#include <algorithm>

std::string ReadFile()
{
    std::ifstream infile("../../05/input.txt");

//    std::string lines;
    std::string line;
    if (infile.is_open())
    {
        while ( getline (infile,line) )
        {
//            line
        }
        infile.close();
    }

    return line;
}

std::unordered_map<char, bool> base_alphabet()
{
    std::unordered_map<char, bool> alpha;

    for(int i = 0; i < 26; ++i)
        alpha.insert(std::make_pair(static_cast<char>('a' + i), false));

    return alpha;
}

void p1x()
{
    const auto input = ReadFile();
    auto alphabet = base_alphabet();

    int i = 0;
    for(int j = 0; i < input.size(); i++)
    {
        // duplicate character
        if(alphabet[input[i]])
        {
            j--;
//            alphabet[input[i]] = false;
            alphabet = base_alphabet();
        }
        // first time character
        else
        {
            j++;
            if(j == 4)
            {
                std::cout << input[i] << std::endl;
                break;
            }
            alphabet[input[i]] = true;
        }
    }
    std::cout << i+1 << std::endl;
}

bool IsUnique(const std::deque<char>& in)
{
    std::string str;

    for(const auto& q : in)
    {
        str +=q;
    }
    std::sort(std::begin(str), std::end(str));
    auto last = std::unique(std::begin(str), std::end(str));
    return last == str.end();
}

void pt1()
{
    const auto input = ReadFile();

    std::deque<char> window;
    char current;

    int i = 0;
    for(; i < input.size(); i++)
    {
        current = input[i];
        window.push_front(input[i]);
        if(window.size() == 5)
        {
            window.pop_back();
        }
        if(window.size() == 4)
        {
            if(IsUnique(window))
                break;
        }
    }

    std::cout << i+1 << std::endl;
}

void p2()
{
    const auto input = ReadFile();

    std::deque<char> window;
    char current;

    int i = 0;
    for(; i < input.size(); i++)
    {
        current = input[i];
        window.push_front(input[i]);
        if(window.size() == 15)
        {
            window.pop_back();
        }
        if(window.size() == 14)
        {
            if(IsUnique(window))
                break;
        }
    }

    std::cout << i+1 << std::endl;
}

int main()
{
//    p1();
    p2();
}