#include <iostream>
#include <random>
#include <cmath>
#include <utility> // For std::pair

using namespace std;

// Generate a random number between a and b
double random_double(double a, double b)
{
    random_device rd;
    mt19937 rng(rd());
    uniform_real_distribution<double> dist(a, b);
    return dist(rng);
}

// Function to minimize/maximize
double func(double x)
{
    // return -pow((2*x-5),4)+pow((x*x-1),3);
    // return -(8+x*x*x-2*x-2*exp(x));
    // return -(4*x*sin(x));
    // return 2 * pow(x - 3, 2) + exp(0.5 * x * x);
    // return x*x-10*exp(0.1*x);
    return -(20*sin(x)-15*x*x);
}

// Derivative of the function (for secant method)
double func_derivative(double x)
{
    // return -8*pow((2*x-5),3)+6*x*pow((x*x-1),2);
    // return -3*x*x+2+2*exp(x);
    // return -4*sin(x)-4*x*cos(x);
    // return 4 * (x - 3) + x * exp(0.5 * x * x);
    // return 2*x-exp(0.1*x);
    return -20*cos(x)+30*x;
}

// Bounding Phase Method
pair<double, double> bounding_phase(double lb, double ub, double delta)
{
    double x = random_double(lb, ub); // Initial random point
    // double x = 0.5;
    cout << "Starting value: " << x << endl;

    double dx = delta;
    double x_lb = max(x - dx, lb);
    double x_ub = min(x + dx, ub);
    double f_x = func(x), f_x_lb = func(x_lb), f_x_ub = func(x_ub);
    int k = 0;

    while (x_ub <= ub && x_lb >= lb)
    {
        dx = (f_x <= f_x_lb && f_x >= f_x_ub) ? abs(dx) : -abs(dx);

        k++;
        double x_new = x + pow(2, k) * dx;
        if (x_new > ub)
            x_new = ub;
        if (x_new < lb)
            x_new = lb;

        if (func(x_new) > f_x)
            return {x, x_new};

        x = x_new;
        x_ub = min(x + abs(dx), ub);
        x_lb = max(x - abs(dx), lb);
        f_x = func(x);
        f_x_lb = func(x_lb);
        f_x_ub = func(x_ub);
    }

    return {x, x};
}

// Secant Method
double secant_method(double x1, double x2, double epsilon)
{
    double z;
    while (true)
    {
        z = x2 - func_derivative(x2) / ((func_derivative(x2) - func_derivative(x1)) / (x2 - x1));
        if (abs(func_derivative(z)) <= epsilon)
            break;
        (func_derivative(z) < 0) ? x1 = z : x2 = z;
    }
    return z;
}

int main()
{
    double lb, ub, epsilon, delta;

    // Input bounds and parameters
    cout << "Enter lower bound: ";
    cin >> lb;
    cout << "Enter upper bound: ";
    cin >> ub;
    cout << "Enter epsilon and delta: ";
    cin >> epsilon >> delta;

    // Perform 10 runs of bounding phase and secant method
    for (int i = 1; i <= 10; i++)
    {
        cout << "Run " << i << " ->" << endl;

        // Bounding phase method
        auto bounds = bounding_phase(lb, ub, delta);
        cout << "Bounding phase result: [" << bounds.first << ", " << bounds.second << "]" << endl;

        // Secant method
        double result = secant_method(bounds.first, bounds.second, epsilon);
        cout << "Secant method result: " << result << endl;
    }

    return 0;
}
