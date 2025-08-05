#include <iostream>
using namespace std;
int main() {
    long long sum = 0;
    for (int i = 0; i < 1000000; i++) sum += i;
    cout << sum << endl;
}
