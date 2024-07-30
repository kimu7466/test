#include<iostream>
using namespace std;

void print_array(int array[], int length){
    for (int i = 0 ; i<length ; i++ ){
        cout << array[i]<< endl; 
    }
}

void insertion_sort(int array[], int length){
    int count =0;
    for (int i = 0; i<length ; i++){
        bool swapped = false;
        int min_index = i;
        for (int j = i+1 ; j<length ; j++ ){
            if (array[j] < array[min_index]){
                int temp = array[j];
                array[j] = array[min_index];
                array[min_index] = temp;
                swapped = true;
            }
        }
    }
}

int main(){
    int array[] = {10,30,40,20,50,15,5,25,45,35};
    int length = sizeof(array)/sizeof(array[0]);

    insertion_sort(array,length);
    print_array(array, length) ;

    return 0;
}

