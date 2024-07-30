#include<iostream>
using namespace std;

void print_array(int array[], int length){
    for (int i = 0 ; i<length ; i++ ){
        cout << array[i]<< endl; 
    }
}

void insertion_sort(int array[], int length){
    for (int i = 1; i<length ; i++){
        int insertion_index = i;
        int current_value = array[i]; 
        int j = i-1;
        for (j; j>=0 && array[j] > current_value ; j-- ){
            array[j+1] = array[j];
            insertion_index = j;
            }
            array[j+1] = current_value; 
        }
    }

int main(){
    int array[] = {10,30,40,20,50,15,5,25,45,35};
    int length = sizeof(array)/sizeof(array[0]);

    insertion_sort(array,length);
    print_array ( array, length );

    return 0;
}

