interface Draw{
void draw();}
class Rectangle implements Draw{
public void draw(){
System.out.println("rectangle drawing");
}}
class Circle implements Draw{
public void draw(){
System.out.println("circle drawing");}
}
class Test{
public static void main(String[] args)
{
Draw d=new Circle();
d.draw();
Draw d1=new Rectangle();
d1.draw();
}}
