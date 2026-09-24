import java.util.*;
class Checksum{
 public static void main(String[]z){
  Scanner s=new Scanner(System.in);
  int n=s.nextInt(),sum=0;
  while(n-->0)sum+=s.nextInt();
  while(sum>255)sum=(sum&255)+(sum>>8);
  System.out.println("Checksum="+(~sum&255));
 }
}
