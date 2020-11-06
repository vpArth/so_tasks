#include <iostream>
#include <math.h>
#include <assert.h>

using namespace std;

namespace mth
{
	template<typename T> class Vector;
	template<typename T>
    Vector<T> operator-(const Vector<T>& v1, const Vector<T>& v2);

    template <typename T>
    class Vector
    {
    private:
        unsigned int length = 0;
        T* buffer = NULL;

    public:
        Vector();
        Vector(const Vector& r);
        Vector(int _length);
        
        ~Vector() { delete[] buffer; }

        void print();

        Vector operator + (const Vector& other);    
        T& operator [] (const int index);

        friend Vector<T> operator-<>(const Vector<T>& v1, const Vector<T>& v2);
    };

    template <class T> Vector<T>::Vector()
    {
        
        length = 1;
        for (auto i = 0u; i < length; i++)
            buffer[i] = 0;
    }

    template <class T> Vector<T>::Vector(int _length)
    {
        length = _length;
        buffer = new T[length];
        for (auto i = 0u; i < length; i++)
            buffer[i] = 0;
    }

    template <class T> Vector<T>::Vector(const Vector & arg)
    {
        
        length = arg.length;
        buffer = new T[length];
        for (auto i = 0u; i < length; i++)
            buffer[i] = arg.buffer[i];
    }

    template<class T> void Vector<T>::print()
    {
        cout << "{ ";
        for (auto i = 0u; i < length; i++)
            cout << "'" << buffer[i] << "' ";
        cout << "}";
    }


    template <class T>
    Vector<T> Vector<T>::operator+(const Vector& arg)
    {
        
        if (length != arg.length)
        {
            cout <<"[ERROR] vectors doesn't match by size"<<endl;
            exit(1);
        }

        Vector<T>temp(length);
        for (auto i = 0u; i < length; i++)        
            temp.buffer[i] = buffer[i] + arg.buffer[i];

        return temp;
    }

    template<typename T>
    T& Vector<T>::operator[](const int index)
    {
        assert(index > -1 && (unsigned)index < length && "Invalid array index");
        return buffer[index];
    }

    template<typename T>
    Vector<T> operator-(const Vector<T>& v1, const Vector<T>& v2)
    {
        //assert(v1.length != v2.length && "The array lengths must be equal");

        Vector<T> temp(v1.length);
        for (int i = 0; i < v1.length; i++)
            temp.buffer[i] = v1.buffer[i] - v2.buffer[i];

        return temp;
    }
}

int main()
{
    mth::Vector<int> example(2);
    mth::Vector<int> example2(2);

    example[0]=1;
    example[1]=2;

    example2[0]=5;
    example2[1]=8;

    mth::Vector<int> example3(example - example2);
    example3.print();

    return 0;
}
