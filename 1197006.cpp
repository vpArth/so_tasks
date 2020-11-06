#include <iostream>
#include <string>

using namespace std;


class JStr {
public:
    std::string str;
    JStr(std::string str): str(str) {}
        friend std::ostream& operator<< (std::ostream& stream, const JStr& self) {
            return stream << "JStr(" << self.str << ")";
        }
};

template <class T> auto convert(T a) {return a;}
template <> auto convert(string a) {return JStr(a);}

template <typename... TArgs> static void foo(TArgs... args) {
    int dummy[sizeof...(TArgs)] = { (std::cout << convert(args) << ", ", 0)... };
}

int main(int argc, char const *argv[])
{
    int a{1};
    string b{"Hello"};

    foo(a, b);

    return 0;
}
