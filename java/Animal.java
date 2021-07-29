class Animal{
void eat(){
System.out.println("eating");
}
}
class Dog extends Animal{
void bark(){
System.out.println("Barking");
}}
class Cat extends Animal{
void meow(){
System.out.println("meowing");
}}
class Main{
public static void main(String[] args){
Cat c=new Cat();
c.eat();
c.meow();
Dog d=new Dog();
d.eat();
d.bark();
}}
