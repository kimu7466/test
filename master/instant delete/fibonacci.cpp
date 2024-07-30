// #include <iostream>
// using namespace std ;

// int main(){
//     int num;
//     int next_digit;
//     cout << "enter a number for print fibonacci series : " ;
//     cin >> num ; 
//     // num = 10;

//     int a = 0;
//     int b = 1 ;
//     cout << a << endl << b << endl ;

//     for (int i = 0 ; i < num-2 ; i++  ){
//         next_digit = a+b;
//         cout << next_digit << endl;
//         a = b ;
//         b = next_digit;
//     }
//     return 0;
// }



// fibonacci series using recursion

#include <iostream>
using namespace std ;

int fibonacci(int num){
    if (num == 0){
        return 0;
    }
    else if( num == 1){
        return 1;
    }
    else{
        return fibonacci(num-1) + fibonacci(num - 2); 
    }
}


int main(){
    int num;
    cout << "enter a number for print fibonacci series : " ;
    cin >> num ; 
    // num = 10;
    for (int i = 0 ; i < num ; i++ ){
    cout << fibonacci(i) << endl ;
    }


    return 0;
}