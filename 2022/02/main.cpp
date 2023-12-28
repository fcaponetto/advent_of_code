#include <fstream>
#include <string>
#include <iostream>
#include <vector>
#include <queue>
#include <map>

std::vector<std::pair<std::string,std::string>> ReadFile()
{
    std::ifstream infile("../../02/input.txt");

    std::vector<std::pair<std::string,std::string>> lines;
    std::string line;
    if (infile.is_open())
    {
        while ( getline (infile,line) )
        {
            auto pos = line.find(" ");
            std::string play1 = line.substr(0, pos);
            std::string play2 = line.substr(line.find(" ")+1);
            lines.push_back(std::make_pair(play1, play2));
        }
        infile.close();
    }

    return lines;
}

void p1()
{
    std::map<std::string, int> player2;

    player2["X"] = 1;
    player2["Y"] = 2;
    player2["Z"] = 3;

    const auto lines = ReadFile();

    int totScore = 0;
    for(const auto& [play1, play2] : lines)
    {
        if((play2 == "X" && play1 == "C") ||
            (play2 == "Y" && play1 == "A") ||
            (play2 == "Z" && play1 == "B"))
        {
            // win
            totScore += 6 + player2[play2];
        }
        else if((play2 == "X" && play1 == "A") ||
                (play2 == "Y" && play1 == "B") ||
                (play2 == "Z" && play1 == "C"))
        {
            // draw
            totScore += 3 + player2[play2];
        }
        else
        {
            // lose
            totScore += player2[play2];
        }
    }

    std::cout << totScore << std::endl;
}

void p2()
{
    std::map<std::string, int> player1, player2;
    player1["A"] = 1;
    player1["B"] = 2;
    player1["C"] = 3;

    const auto lines = ReadFile();

    int totScore = 0;
    for(const auto& [play1, play2] : lines)
    {
        if(play2 == "X")
        {
            // lose
            totScore += ((player1[play1]+2)%3) + 1;
        }
        else if(play2 == "Y")
        {
            // draw
            totScore += 3 + player1[play1];
        }
        else
        {
            // win
            totScore += 6 + ((player1[play1]+1)%3) + 1;
        }
    }

    std::cout << totScore << std::endl;
}

int main()
{
    p2();
}