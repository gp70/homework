#include <iostream>
#include <string>
using std::cout;
using std::endl;
using std::string;

void line(int a, char c)
{
  	string s(a + 1, c);
	cout << s << "\n";
}

void rect(int r, int c)
{
  	string s(c + 1, '#');
	for(int i = 0; i < r; ++i)
	{
		std::cout << s << "\n";
	}
}

/*

 *
 **
 ***
 ****

 */
void tri1(int h)
{
	for(int i = 0; i < h; ++i)
	{
		for(int j = 0; j < (i + 1); ++j)
		{
			cout << "*";
		}
	cout << "\n";
	}
}


/*
   *
  ***
 *****
 */
void tri2(int h)
{
     for (int i = 0; i < h; ++i)
     {
		cout << string(h - i,' ');
		for(int j = 0; j < (i + 1); ++j)
		{
			cout << "*" << ' ';
		}
		cout << "\n";
     }
}

/*
  *
 **
***
 */
void tri3(int h)
{
	for(int i = 0; i < h; ++i)
	{
		cout << string(h - i,' ');
		for(int j = 0; j < (i + 1); ++j)
		{
			cout << "*";
		}
	cout << "\n";
	}
}

void piglatinify()
{
	std::cout << "Enter a string: ";
	std::string s;
	std::cin >> s;
	std::cout << s.c_str() + 1 << s[0] << "ay" << "\n";
}

int main()
{
  line(5,'#');
  cout << "\n";
  rect(3,5);
  cout << "\n";
  tri1(6);
  cout << "\n";
  tri2(5);
  cout << "\n";
  tri3(7);
  cout << "\n";
  piglatinify();
}