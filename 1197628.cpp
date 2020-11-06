#include <iostream>
#include <cstdio>

using namespace std;

const int N = 7;
const int M = 7;
int A[N][M] = {
    {-2, 1, 2, 3, 2, 0, -4},
    {-5, 1, 3, -1, -3, -5, 3},
    {-2, 4, 5, -5, 1, 1, -1},
    {4, 2, -2, 2, -5, -5, -2},
    {2, -1, -2, -1, 1, -1, -1},
    {-5, -2, 5, 3, 2, -1, 3},
    {-3, -1, 1, 2, -4, 3, -2}
};



int main() {
	auto len = N*M;
	for (auto index1 = 0, index2 = 1; index1 < len && index2 < len; ++index1, ++index2) {
		auto i = index1 / N;
		auto j = index1 % N;
		if (A[i][j] >= 0) {
			for (; index2 < N*M; ++index2) {
				auto k = index2 / N;
				auto l = index2 % N;
				if (A[k][l] < 0) {
					swap(A[i][j], A[k][l]);
					break;
				}
			}
		}
	}

	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < M; ++j) {
			cout << A[i][j] << " ";
		}
		cout << "\n";
	}
}


