//
//  main.c
//  test
//
//  Created by retinderdeep singh on 17/04/20.
//  Copyright © 2020 retinderdeep singh. All rights reserved.
//

#include <pthread.h>
#include<stdio.h>
void do_one_thing(int *);
void do_another_thing(int *);
void do_wrap_up(int, int);

int r1 = 0, r2 = 0;


int main()
{
    pthread_t thread1, thread2;
    
    pthread_create(&thread1,NULL,(void *) do_one_thing,(void *) &r1);
    
    pthread_create(&thread2,NULL,(void *) do_another_thing,(void *) &r2);
    
    pthread_join(thread1, NULL);
    pthread_join(thread2, NULL);
    
    do_wrap_up(r1, r2);
    
}

void do_one_thing(int *pnum_times)
{
    printf("welcome\n");
    
}

void do_another_thing(int *pnum_times)
{
    int a,b,c;
    printf("Enter the value of a : ");
    scanf("%d", &a);
    printf("Enter the value of b : ");
    scanf("%d", &b);
    c= a+b;
    printf("sum of a and b is : %d\n",c);
    
}

void do_wrap_up(int one_times, int another_times)
{
    printf("Thankyou\n");
}
