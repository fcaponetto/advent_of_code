#include <fstream>
#include <string>
#include <iostream>
#include <vector>
#include <queue>
#include <map>

struct Section
{
    int id1;
    int id2;
};

void SplitStringWithDelimiter(const std::string& in, const std::string& delim, std::string& out1, std::string& out2)
{
    auto pos = in.find(delim);
    out1 = in.substr(0, pos);
    out2 = in.substr(in.find(delim)+1);
}

std::vector<std::pair<Section,Section>> ReadFile()
{
    std::ifstream infile("../../03/input.txt");

    std::vector<std::pair<Section,Section>> lines;
    std::string line;
    if (infile.is_open())
    {
        while ( getline (infile,line) )
        {
            const auto delim1 = ",";
            const auto delim2 = "-";
            std::string interval1, interval2, sec1, sec2;
            SplitStringWithDelimiter(line, delim1, interval1, interval2);
            SplitStringWithDelimiter(interval1, delim2, sec1, sec2);
            Section section1 = {atoi(sec1.c_str()), atoi(sec2.c_str())};
            SplitStringWithDelimiter(interval2, delim2, sec1, sec2);
            Section section2 = {atoi(sec1.c_str()), atoi(sec2.c_str())};

            lines.push_back(std::make_pair(section1, section2));
        }
        infile.close();
    }

    return lines;
}

void p1()
{
    const auto sections = ReadFile();

    int retOverlapPair = 0;

    for(const auto& [section1, section2] : sections)
    {
        int id1L = section1.id1;
        int id1R = section1.id2;
        int id2L = section2.id1;
        int id2R = section2.id2;

        // one of the section is contained within the other one
        if( ((id1L <= id2L) && (id1R >= id2R)) ||
            ((id1L >= id2L) && (id1R <= id2R)))
        {
            retOverlapPair++;
        }
    }

    std::cout << retOverlapPair << std::endl;
}

void p2()
{
    const auto sections = ReadFile();

    int retOverlapPair = 0;

    for(const auto& [section1, section2] : sections)
    {
        int id1L = section1.id1;
        int id1R = section1.id2;
        int id2L = section2.id1;
        int id2R = section2.id2;

        // not overlap at all
        if( (id1R < id2L) ||
            (id1L > id2R))
        {
            retOverlapPair++;
        }
    }

    std::cout << sections.size() - retOverlapPair << std::endl;
}

int main()
{
    p1();
    p2();
}