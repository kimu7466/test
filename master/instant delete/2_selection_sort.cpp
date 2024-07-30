#include<iostream>
using namespace std;

void selection_sort(int array[], int length){
    for ( int i = 0 ; i < length-1 ; i++ ){
        int min_index = i;
        for (int j = i+1 ; )
    }    
}

void print_array(int array[], int length){
    for( int i = 0 ; i < length ; i++){
        cout << array[i] << endl;
    }
}
int main(){
    int array[] = {10,50,70,60,20,80,30,40};
    int length = sizeof(array)/ sizeof(array[0]);

    selection_sort(array, length);
    print_array(array,length);

    return 0;
}