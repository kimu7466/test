#include<iostream>
using namespace std;

void print_array(int array[], int length){
    for (int i = 0 ; i<length ; i++ ){
        cout << array[i]<< endl; 
    }
}

void bubble_sort(int array[], int length){
    for ( int i = 0 ; i<length ; i++ ){   
        bool swap = false;  
        for ( int j = 0 ; j<length-i-1 ; j++ ){
            if (array[j] > array[j+1]){
                int temp = array[j];
                array[j] = array[j+1];
                array[j+1] = temp;
                swap = true;
            }
        }
        if (!swap){
            break;
        }
    }

}

int main(){
    int array[] = {10,30,40,20,50,15,5,25,45,35};
    int length = sizeof(array)/sizeof(array[0]);

    bubble_sort(array,length);

    print_array(array, length);
    return 0;
}

