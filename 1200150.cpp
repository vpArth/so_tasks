#include <iostream>

using namespace std;

void print_rect(int width, int height) {
    for (int i = 0; i < height; ++i) {
        for (int j = 0; j < width; ++j) {
            bool border = i == 0 || j == 0 || i+1 == height || j+1 == width;
            cout << (border ? '*' : ' ');
        }
        if (width != 0) cout << '\n';
    }
}

int main()
{
    print_rect(10, 3);
    print_rect(5, 1);
    print_rect(0, 10);
    print_rect(3, 0);
}
