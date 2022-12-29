#include <fstream>
#include <string>
#include <iostream>
#include <vector>
#include <queue>
#include <map>
#include <unordered_map>
#include <set>
#include <algorithm>

struct Index
{
    int value;
    bool visible;
};

std::vector<std::vector<int>> ReadFile()
{
    std::ifstream infile("../../07/input_simple.txt");

    std::vector<std::vector<int>> matrix;
    std::string line;
    if (infile.is_open())
    {
        while ( getline (infile,line) )
        {
            std::vector<int> tmp;
            for(int i=0; i < line.size(); i++)
            {
                tmp.push_back(line[i] - '0');
            }
            matrix.push_back(tmp);
        }
        infile.close();
    }

    for(int i = 0; i < matrix.size(); i++)
    {

    }

    return matrix;
}

bool legal(int y, int x) {
    return y >= 0 && x >= 0 && y < 99 && x < 99;
}

void p1()
{
    auto matrix = ReadFile();

    using namespace std;

    int ans = 0;
    vector<pair<int, int>> dirs = {{-1, 0}, {0, -1}, {1, 0}, {0, 1}};
    for (int i = 0; i < matrix.size(); i++) {
        for (int j = 0; j < matrix[i].size(); j++) {
            bool visible = false;
            for (int k = 0; k < 4; k++) {
                int tmp = 1;
                while (
                    legal(i + tmp*dirs[k].first, j + tmp*dirs[k].second) &&
                    matrix[i + tmp*dirs[k].first][j + tmp*dirs[k].second]
                    < matrix[i][j])
                {
                    std::cout << i << "  " << j << "  " << k <<  std::endl;
                    tmp++;
                }

                visible |= !legal(i + tmp*dirs[k].first, j + tmp*dirs[k].second);
            }
            if (visible)
                ans++;
        }
    }

    cout << ans << endl;
}

void p2()
{
    const auto input = ReadFile();

}

int main()
{
    p1();
    p2();
}