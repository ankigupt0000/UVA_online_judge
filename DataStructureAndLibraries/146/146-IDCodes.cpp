#include <iostream>
#include <cstring>
#include <algorithm>
#include <cstdio>
using namespace std;
int main()
{
    char mychar[50];
    int i;
    while(1)
    {
        cin >> mychar;
        if(strcmp(mychar,"#")==0)
        {
            break;
        }
        if(next_permutation(mychar,mychar+strlen(mychar)))
        {
            cout << mychar << endl;
        }
        else
        {
            cout << "No Successor" << endl;
        }
    }
    return 0;
}
