//interfaces
interface print{
void print();
}
class AA implements print{
 public void print(){
System.out.print("hello");
}
public static void main(String[] args){
AA obj=new AA();
obj.print();
}}