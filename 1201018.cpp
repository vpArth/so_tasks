#include <iostream>

int main()
{
    srand(time(0));
    for (auto i = 0; i < 20; ++i) {
        std::cout << (rand() % (10000-1000+1) + 1000) << std::endl;
    }
}
