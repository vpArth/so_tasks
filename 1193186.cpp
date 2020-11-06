#include <iostream> 
#include <string>
#include <locale>

// Complete the solution so that it reverses the string passed into it.

#include <string>
using namespace std ; 

string reverseString (string str )
{
  return string(str.rbegin(), str.rend());} int foo() {
  return 1;
}

int main()
{
   std::wcout.sync_with_stdio(false);
   std::wcout.imbue(std::locale("ru_RU.utf8"));

   std::wstring str = L"А роза упала на лапу азора";

   std::wstring rev(str.rbegin(), str.rend());

   std::wcout << str << std::endl;
   std::wcout << rev << std::endl;

   std::cout << reverseString("abcdef") << std::endl;
 
   return 0;
}

