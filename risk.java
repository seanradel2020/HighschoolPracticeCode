
import java.io.*;
import java.util.*;
public class risk
{
    public int age;
    public String married;
    public int children;
    public int retAge; 
    public double riskApp; 
    public int yearsUntilRet = 0;
    public double calcRiskApp;
    public int riskTotal=0;
    
    public void toRisk() {
    
    Scanner kbReader = new Scanner(System.in);
    
    System.out.println("How old are you?");
    int age = kbReader.nextInt();
    
    System.out.println("At what age would you like to retire?");
    int retAge = kbReader.nextInt();
    
    int yearsUntilRet = retAge - age;
    
    if(yearsUntilRet<=10)
    riskTotal = riskTotal + 1; 
    else if(yearsUntilRet>10 && yearsUntilRet<=17)
    riskTotal = riskTotal + 2;
    else if(yearsUntilRet > 17)
    riskTotal = riskTotal + 3;
    
    
    System.out.println("Are you married?");
    String married = kbReader.next();
    
    System.out.println("How many children do you have?");
    int children = kbReader.nextInt();
    
    if(married.equalsIgnoreCase("yes")) 
    riskTotal = riskTotal + 2;

    if(married.equalsIgnoreCase("no"))
    riskTotal = riskTotal + 3;
    
    if(children<=2 && age>21)
    riskTotal = riskTotal + 2;
    
    if(children==0)
    riskTotal = riskTotal + 3;
    
    if(children!=0 && age<=21)
    riskTotal = riskTotal + 1;
    
    if(children>2)
    riskTotal = riskTotal + 1; 
    
    double calcRiskApp= riskTotal/3;
    
    System.out.println("What is your risk appetite?");
    riskApp = kbReader.nextDouble(); 
     System.out.println("Your calculated risk appetite is: " + calcRiskApp);
    
    if(riskApp>calcRiskApp)
    System.out.println("Your risk appetite is too risky");
    if(riskApp==calcRiskApp)
    System.out.println("What is your risk appetite is just right");
    if(riskApp<calcRiskApp)
    System.out.println("You can be more risky");
    
    
}
    
    
}