//multiple
class A{
void msg(){
System.out.println("hello");
}
}
class B{
void msg(){
System.out.println("Welcome");}}
class C extends A, B{
public static void main(String []args){
C c=new C();
c.msg();
}}
