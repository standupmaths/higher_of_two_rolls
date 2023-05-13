#include <iostream>
#include <random>
#include <ctime>

using namespace std;

int main() {
    int number_of_sides;
    cout << "How many sides on your dice? ";
    cin >> number_of_sides;

    double t1 = clock();

    float sum_results = 0;

    int trials = 1000000;

    for (int i = 0; i < trials; i++) {
        sum_results += max(rand() % number_of_sides + 1, rand() % number_of_sides + 1);
    }

    cout << "Average result of rolling two and taking the highest is " << sum_results / trials << endl;
    cout << "Time taken: " << (clock() - t1) / CLOCKS_PER_SEC << " seconds" << endl;
}