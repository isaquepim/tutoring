#include<iostream>
#include<stdlib.h>
#include<math.h>


using namespace std;

float random()
{
    return (float) rand() / (RAND_MAX+1);
}

int poisson(float lambda)
{
    int sum = 0;
    float accum = 1;
    float u;

    accum *= u;
    while(accum > exp(-lambda))
    {
        u = random();
        sum++;
        accum *= u;
    }
    return sum;
}

int main()
{
    float l, p, u;
    int n = 10;
    float sum = 0;

    for(int i = 0; i < n; i++)
    {
        l = random()*3;
        p = poisson(l);

        if(p == 0.0) sum++;
    }

    cout << sum/n << endl;

    return 0;
}