class Stringjava{
    public static void main(String [] args){
        String s1="hello";     //literal
        char ch[]={'s','t','r','i','n', 'g'};
    String s2=new String(ch);    //converting char array to string
    String s3=new String("example");//creating string by new keyword
    System.out.println(s1);
    System.out.println(s2);
    System.out.println(s3);
char ch1=s1.charAt(3);
System.out.println(ch1);
int l=s2.length();
System.out.println("length of s2: "+l);
String s=s1.substring(1, 4);
System.out.println(s);
    }
}
//1. toUpperCase()
//2. toLowerCase()


//4. concat(String s3)
//5. s1.replace(char old, char new);
//6. indexOf(char)