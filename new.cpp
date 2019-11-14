#include<iostream>
const int strsize=20;
struct bop{
	char fullname[strsize];
	char title[strsize];
	char bopname[strsize];
	int preference;
};
int main()
{
	using namespace std;
	cout<<"BenevolentOrderofProgrammersReport\n"
	<<"a.displaybyname
	b.displaybytitle\n"
	<<"c.displaybybopname
	d.diplaybypreference\n"
	<<"q.quit\n";
	char ch;
	bopmember[5]={
		{"WimpMacho","EnglishTeacher","DEMON",0},
		{"RakiRhodes","JuniorProgrammer","BOOM",1},
		{"CeliaLaiter","SuperStar","MIPS",2},
		{"HoppyHipman","AnalystTrainee","WATEE",1},
		{"PatHand","Police","LOOPY",2}
	};
	cout<<"Enteryourchoice:";
	while(cin>>ch&&ch!='q')
	{
		switch(ch)
		{
			case 'a':
			for(inti=0;i<5;i++)
			cout<<member[i].fullname<<endl;
			break;
			case 'b':
			for(inti=0;i<5;i++)
			cout<<member[i].title<<endl;
			break;
			case 'c':
			for(inti=0;i<5;i++)
			cout<<member[i].bopname<<endl;
			break;
			case 'd':
			for(inti=0;i<5;i++)
			{
				if(member[i].preference==0)
				cout<<member[i].fullname<<endl;
				elseif(member[i].preference==1)
				cout<<member[i].title<<endl;
				elseif(member[i].preference==2)
				cout<<member[i].bopname<<endl;
			}
			break;
		}
		cout<<"Nextchoice:";
	}
	cout<<"Bye!\n";
	return 0;
}