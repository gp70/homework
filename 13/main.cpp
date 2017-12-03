#include <stdio.h>
#include <iostream>
#include <list>

int caught_speeding(int speed,bool isbday)
{
	if(isbday)
		speed = speed - 5;
	if(speed<=60)
		return 0;
	if(speed<=80)
		return 1;
	return 2;
}

int lucky_sum(int a,int b,int c)
{
	int list[] = {a,b,c};
	int sum = 0;
	for(int i=0;i<3;i++)
	{
		if(list[i] == 13)
			return sum;
		sum += list[i];
	}
	return sum;
}

bool love6(int a,int b)
{
	if((a == 6) || (b == 6) || (a + b == 6) ||
	   (a - b == 6) || (b - a == 6))
	{
		return true;
	}
	return false;
}

int main()
{
	std::cout << "Should be 0: " << 
	caught_speeding(61,true) << "\n"
	<< "Should be 1: " << 
	caught_speeding(61,false) << "\n"
	<< "Should be 2: " <<
	caught_speeding(99,true) << "\n";
	
	std::cout << "Should be 6: " <<
	lucky_sum(1,2,3) << "\n" <<
	"Should be 3: " << lucky_sum(1,2,13)
	<< "\n" << "Should be 1: " << 
	lucky_sum(1,13,3) << "\n";
	
	std::cout << "Should be true (1): " <<
	love6(6,4) << "\n" << "Should be false (0): "
	<< love6(4,5) << "\n" <<
	"Should be true (1): " << love6(1,5) << "\n";
	
	return 0;
}