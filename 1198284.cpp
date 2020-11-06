#include <cstdlib>
#include <string>
#include <iostream>
#include <cassert>

using namespace std;

string divmod(const string &input, const int n, int &mod) {
    assert(n > 1);
    string res;
    string divided;

    for (auto c: input) {
        divided += c;
        auto r = div(stoi(divided), n);
        if (r.quot != 0) {
            res += (r.quot + '0');
        } else if (res.length()) res += '0'; // skip leading 0

        divided = to_string(r.rem);
    }

    mod = stoi(divided);
    return res;
}

string dec2n(string input, const int n) {
    assert(n <= 62 && n > 1);
    string res;
    int mod;
    while (input.length()) {
        input = divmod(input, n, mod);
        res = (char)(mod + (mod < 10 ? '0' : (mod < 36 ?'a'-10:'A'-36))) + res;
    }

    return res;
}

int main(int argc, char const *argv[])
{
    int mod = 0;
    { auto d = divmod("10000000000000000000000000001", 2, mod); cout << d << ", " << mod << endl; }
    { auto d = divmod("22222222222222222222222222222", 2, mod); cout << d << ", " << mod << endl; }
    { auto d = divmod("82734682736482638476238476237", 2, mod); cout << d << ", " << mod << endl; }
    { auto d = dec2n("82734682736482638476238476237", 2); cout << d << endl; }
    { auto d = dec2n("1120175546223060130598879262554599764676229330351202023251910795166237121851795753689981066816411931661406295196294425474326181163776482575744054010948427561942575245782787742816421059855869212856715454123140043866392208776553004037021851895189704871507624871254033251309082668594716363388202777292967624069500740955581776209433563237536482725004063297910761839642728715573454854615414489086732463316913397879117051391977140598698313669359648529491927340819656031084171447299111728694528002", 3); cout << d << endl; } // 3 ** 1025 - 3 ** 512
    { auto d = dec2n("1032", 2); cout << d << endl; }
    { auto d = dec2n("42535295865117307932921825928971026433", 2); cout << d << endl; }
    { auto d = dec2n("359538626972463181545861038157804946723595395788461314546860162315465351611001926265416954644815072042240227759742786715317579537628833244985694861278948248755535786849730970552604439202492188238906165904170011537676301364684925762947826221081654474326701021369172596479894491876959432609670712659248448274433", 2); cout << d << endl; }
    { auto d = dec2n("295990750022427673183926996510285089534", 16); cout << d << endl; } // 0xDEADBEAFFEEDD00D000000000DADCAFE
    { auto d = dec2n("1050215907863349821", 62); cout << d << endl; } // 1fA0000000Z

    return 0;
}
