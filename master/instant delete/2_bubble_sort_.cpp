// #include <iostream>

// using namespace std;

// void bubble_sort(int array[], int length){
//         int count = 0;
//     for( int i = 0 ; i<length ; i++){
//         bool swapped = false;
//         for (int j = 0 ; j<length-i -1; j++ ){
//             if ( array[j] > array[j+1]){
//                 int temp = array[j];
//                 array[j] = array[j+1];
//                 array[j+1] = temp;
//                 count++;
//                 swapped = true;
//             }
//         }
//         if (swapped == false){
//             break;
//         }
//     }
//     cout << "count : " << count << endl;
// }

// void print_array(int array[], int length){
//     for (int i = 0; i<length; i++){
//         cout << array[i] << endl;
//     }
// }

// int main(){
//     int array[] = {40,50,20,30,60,10};

//     int length = sizeof(array)/ sizeof(array[0]);

//     bubble_sort(array, length);

//     print_array(array, length); 

//     return 0;
// }



#include <iostream>
using namespace std;

void bubble_sort(int array[], int length) {
    int count = 0;
    for (int i = 0; i < length; i++) {
        bool swapped = false;
        for (int j = 0; j < length - i - 1; j++) {
            if (array[j] > array[j + 1]) {
                int temp = array[j];
                array[j] = array[j + 1];
                array[j + 1] = temp;
                count++;
                swapped = true;
            }
        }
        if (!swapped) {
            break;
        }
    }
    cout << "count: " << count << endl;
}

void print_array(const int array[], int length) {
    for (int i = 0; i < length; i++) {
        cout << array[i] << " ";
    }
    cout << endl;
}

int main() {
    int array[] = {50, 40, 30, 10};
    int length = sizeof(array) / sizeof(array[0]);

    bubble_sort(array, length);
    print_array(array, length);

    return 0;
}
