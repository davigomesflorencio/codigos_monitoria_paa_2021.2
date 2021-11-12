#include <bits/stdc++.h>

// #include <iostream>
using namespace std;

int potenciacao(int b, int n)
{

    if (n == 1)
        return b;
    if (n == 0)
        return 1;
    else if (n % 2 == 0)
        return potenciacao(b, n / 2) * potenciacao(b, n / 2);
    else
        return b * potenciacao(b, n / 2) * potenciacao(b, n / 2);
}

int potenciacao2(int b, int n)
{
    if (n == 1)
        return b;
    if (n == 0)
        return 1;
    else
    {
        int s = potenciacao2(b, n / 2);
        if (n % 2 == 0)
            return s * s;
        else
            return b * s * s;
    }
}

int main()
{

    int b = 0, n = 0, potencia = 0;
    cout << "Informe o valor de b: ";
    cin >> b;
    cout << "informe o valor de n: ";
    cin >> n;

    potencia = potenciacao2(b, n);
    cout << potencia << endl;
}
