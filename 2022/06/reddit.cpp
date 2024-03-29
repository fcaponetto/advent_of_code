#include <iostream>
#include <fstream>
#include <vector>
#include <memory>
#include <stddef.h>

class Directory
{
public:
    Directory *parent;
    std::vector<Directory *> subdirs;
    std::string name;
    size_t size; // does not include subdir sizes

    Directory()
    {
        size = 0;
        parent = nullptr;
        name = "";
    }

    const size_t computeTotalSize() const
    {
        size_t totalSize = size;
        for (const auto dir : subdirs)
            totalSize += dir->computeTotalSize();
        return totalSize;
    }

    void addSubDirectory(const std::string &newDirectoryName)
    {
        Directory *newSubDirectory = new Directory();
        newSubDirectory->name = newDirectoryName;
        newSubDirectory->parent = this;
        subdirs.push_back(newSubDirectory);
    }

    void deleteSubDirectories()
    {
        for (auto dir : subdirs) {
            dir->deleteSubDirectories();
            delete dir;
        }
    }

    size_t findDirectory(const std::string &name)
    {
        for (size_t i = 0; i < subdirs.size(); i++)
            if (subdirs[i]->name == name) return i;
        std::cout << "Could not find directory\n";
        return 0;
    }
};

size_t sumOfSmallDirectories(const Directory *head, size_t maxSize)
{
    size_t total = 0;
    for (const auto dir : head->subdirs)
        total += sumOfSmallDirectories(dir, maxSize);

    if (head->computeTotalSize() <= maxSize)
        total += head->computeTotalSize();
    return total;
}

size_t sizeofSmallestDirectoryToDelete(const Directory *head,
                                       size_t sizeNeeded)
{
    size_t smallest = SIZE_MAX;
    for (const auto dir : head->subdirs) {
        size_t otherSmallest = sizeofSmallestDirectoryToDelete(dir, sizeNeeded);
        if (otherSmallest < smallest) smallest = otherSmallest;
    }

    size_t size = head->computeTotalSize();
    if (size >= sizeNeeded && size <= smallest) smallest = size;
    return smallest;
}

int main(void)
{
    std::ifstream commandsFile("../../06/input.txt");
    std::string command, skip, nextDirectory;
    Directory home;
    home.name = "/";
    Directory *currentDir = &home;
    bool cd = false;

    getline(commandsFile, command); // ignore first line
    while (getline(commandsFile, command)) {
        if (command.substr(0, 4) == "$ cd") {
            cd = true;
            nextDirectory = command.substr(5);
        }

        if (cd && nextDirectory == "..") {
            currentDir = currentDir->parent;
            cd = false;
            continue;
        } else if (cd) {
            currentDir = currentDir->subdirs[currentDir->findDirectory(nextDirectory)];
            cd = false;
            continue;
        }

        if (command.substr(0, 4) == "$ ls") continue;

        if (command.substr(0, 3) == "dir") {
            currentDir->addSubDirectory(command.substr(4));
            continue;
        }

        // file
        currentDir->size += stoi(command.substr(0, command.find(" ")));
    }

    std::cout << sumOfSmallDirectories(&home, 100'000) << "\n";

    size_t memoryAvailable = (70'000'000 - home.computeTotalSize());
    size_t numNeeded = 30'000'000 - (70'000'000 - home.computeTotalSize());
    std::cout << "Space unused: " << memoryAvailable << std::endl;
    std::cout << "Space needed: " << numNeeded << "\n";
    std::cout << "Size of smallest directory to delete: "
              << sizeofSmallestDirectoryToDelete(&home, numNeeded) << "\n";

    home.deleteSubDirectories();
}