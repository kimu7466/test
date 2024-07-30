// #include <iostream>
// using namespace std ;

// int main(){
//     bool operation = true;
//     while (operation)
//     {
//     int num;
    
//     cout << "enter a number to print factorial : " ;
//     cin >> num ; 

//     // num = 5;
//     int fact = 1;

//     for (int i = num ; i>0 ; i--){
//         fact *= i;
//     }
//     cout <<fact<< endl;
//     int ans;
//     cout << "do you want to perform again (0 to cancel) : ";
//     cin >> ans;
//     if (ans == 0){
//         operation = false;
//     }
//     else{
//         operation = true;
//     }
//     }
//     return 0;
// }



// factorial with recursion


#include <iostream>
using namespace std ;

int factorial(int num){
    if (num == 0  || num == 1){
        return 1;
    }
    else{
        return num * factorial(num-1);
    }
}


int main(){
    int num;    
    cout << "enter a number to print factorial : " ;
    cin >> num ; 

    // num = 5;
    cout << factorial(num) << endl ;

    return 0;
}
