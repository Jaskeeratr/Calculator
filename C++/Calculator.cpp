#include <iostream>
#include <cmath>

using namespace std;

double basic_operations(double a, double b, char operation) {
    switch (operation) {
        case '+': return a + b;
        case '-': return a - b;
        case '*': return a * b;
        case '/': return (b != 0) ? a / b : NAN;
        default: return NAN;
    }
}

double advanced_operations(double a, string operation) {
    if (operation == "sqrt") return sqrt(a);
    else if (operation == "log") return log(a);
    else if (operation == "exp") return exp(a);
    else if (operation == "sin") return sin(a);
    else if (operation == "cos") return cos(a);
    else if (operation == "tan") return tan(a);
    else return NAN;
}

int main() {
    double a, b;
    char operation;
    string mode, adv_operation;

    cout << "Choose mode: basic or advanced?\n";
    cin >> mode;

    if (mode == "basic") {
        cout << "Enter first number: ";
        cin >> a;
        cout << "Enter operation (+, -, *, /): ";
        cin >> operation;
        cout << "Enter second number: ";
        cin >> b;
        cout << "Result: " << basic_operations(a, b, operation) << endl;
    } else if (mode == "advanced") {
        cout << "Enter number: ";
        cin >> a;
        cout << "Enter operation (sqrt, log, exp, sin, cos, tan): ";
        cin >> adv_operation;
        cout << "Result: " << advanced_operations(a, adv_operation) << endl;
    } else {
        cout << "Invalid mode!";
    }

    return 0;
}
