// #include<iostream>
// using namespace std;

// int sum_array(int array[], int length){
//     int sum_ = 0;
//     for (int i = 0 ; i < length ; i++ ){
//         sum_ += array[i] ;

//     }
//     return sum_;
// }


// int main(){
//     int array[] = {2,2,2,2,2};
//     int length = sizeof(array)/sizeof(array[0]);

//     cout << sum_array(array, length);

//     return 0;
// }

// sum of array using recurrsion

#include<iostream>
using namespace std;

int sum_array(int array[], int length){
    if ( length == 0 ){
        return 0;
    }
    else{
        return array[0] + sum_array(array+1, length-1);
    }
}


int main(){
    int array[] = {2,2,2,2,2,2};
    int length = sizeof(array)/sizeof(array[0]);

    cout << sum_array(array, length);

    return 0;
}