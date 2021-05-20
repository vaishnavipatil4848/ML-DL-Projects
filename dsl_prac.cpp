#include<iostream>
using namespace std;

struct node
{
    bool bit;
    node *next,*prev;
};
class dll 
{
    public:
    node *head1, *head2,*head3;
    node* create(node*);
    void read();
    void print(node*);
    void printno();
    void addno();
    node* add(node*,node*);
    dll()
    {
        head1=head2=head3=NULL;
    }
};
void dll::read()
{
    cout<<"1st binary number:\n";
    head1=create(head1);
    cout<<"2nd binary nmber:\n";
    head2=create(head2);
}
node* dll:: create(node *temp)
{
    int n;
    node *temp1,*last;
    cout<<"Enter total No. of bits:\n";
    cin>>n;
    for(int i=0;i<n;i++)
    {
        temp1=new node;
        cout<<"Enter value of bit:\t";
        cin>>temp1->bit;
        temp1->prev=NULL;
        temp1->next=NULL;

        if(temp==NULL)
        {
            temp=temp1;
            last=temp1;
        }
        else
        {
            last->next=temp1;
            temp1->prev=last;
            last=temp1;
        }
    }
    return(temp);
}
void dll::addno()
{
    cout<<"Addition\n";
    head3=add(head1,head2);
    print(head3);
}
node* dll:: add(node *temp1,node *temp2)
{
    int c,sum,bit1,bit2;
    node *temp3;
    if(temp1!=NULL && temp2==NULL)
        head3=temp1;
    else if(temp1==NULL && temp2!=NULL)
        head3=temp2;
    else
    {
        c=0;
        sum=0;
        while(temp1->next!=NULL)
          temp1=temp1->next;
        while(temp2->next!=NULL)
          temp2=temp2->next;

        while(temp1!=NULL || temp2!=NULL)
        {
            if(temp1!=NULL)
               bit1=temp1->bit;
            else
               bit1=0;
            if(temp2!=NULL)
               bit2=temp2->bit;
            else
               bit2=0;
            
            sum=bit1+bit2+c;
            c=sum/2;
            sum=sum%2;

            temp3=new node;
            temp3->bit=sum;
            temp3->next=temp3->prev=NULL;

            if(head3==NULL)
            {
                head3=temp3;
            }
            else
            {
               temp3->next=head3;
               head3->prev=temp3;
               head3=temp3; 
            }
            if(temp1!=NULL)
               temp1=temp1->prev;
            if(temp2!=NULL)
               temp2=temp2->prev;
        }
        if(c==1)
        {
            temp3=new node;
            temp3->bit=c;
            temp3->next=temp3->prev=NULL;
            temp3->next=head3;
            head3->prev=temp3;
            head3=temp3;
        }
    }
    return(head3);
}
void dll::printno()
{
    cout<<"1st binary number:\n";
    print(head1);
    cout<<"\n";
    cout<<"2nd binary number:\n";
    print(head2);
    cout<<"\n";
}
void dll:: print(node *t)
{
    if(t==NULL)
       cout<<"Empty";
    else
    {
        while(t!=NULL)
        {
            cout<<t->bit<<" ";
            t=t->next;
        }
    }
}
int main()
{
    dll d;
    d.read();
    d.printno();
    d.addno();
    return 0;
}