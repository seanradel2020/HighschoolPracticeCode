
/**
 * Stock Program
 *
 * Sean Radel
 * March 11, 2019
 */
import java.io.*;
import java.util.*;
//import java.util.ArrayList;
public class stockMain
{
     public static void main(String args[])throws IOException{
    Scanner kbReader= new Scanner(System.in); //starting the scanner
    /*System.out.println("Stocks?");
    *boolean risk= kbReader.nextBoolean();
   */
   
  String stockTicker;
String stockName;
double stockPrice;
int stockRisk;
  
  char riskMan;
  float riskHelper = 0;
  int j = 0;
  ArrayList<String> stockList = new ArrayList<String>();
 ArrayList<String> investorList = new ArrayList<String>();
  ArrayList<portfolioStocks> stockObject = new ArrayList<portfolioStocks>();
  // String[] stocks = new stocks[2957];
  //personClass newInvestor = new personClass(true,10);
 
  File file = new File("C:\\Users\\sradel\\Desktop\\stockMan\\stocks2.txt");
 
  BufferedReader br = new BufferedReader(new FileReader(file));
 
  String st;
  while ((st = br.readLine()) != null) {
    System.out.println(st);
   //lines.add(st);
   stockList.add(st);
   //System.out.println(lines);
  
}
System.out.println("Would you like to invest in any stocks? (true or false)");
boolean investTrueOrFalse= kbReader.nextBoolean();
 System.out.println("What stocks would you like to invest in? (ticker)");
while(investTrueOrFalse == true){
    
   // System.out.println("What stocks would you like to invest in? (ticker)");
  String tickerHelper =  kbReader.next();
   //String helpTick = stockList.get(j);
  // String tickerHelper2 = helpTick.split(",");
  //Scanner scan = new Scanner(helpTick);
  //scan.useDelimiter(",");
  //String tickerHelper2= scan.next();
  for(int q = o; q<Stocklist.size; q++){
      if(stockHelper.get(q).ticker==tickerHelper){
         investorList.add(stockList[q]); 
        }
     
      
    }
  //if(tickerHelper == tickerHelper2){
      
      
      
      
       String addedStock = stockList.get(j);
       // String addedStock = stockList.get(j);

    
         investorList.add(addedStock);
    
 System.out.println("Would you like to invest in any more stocks? (true or false)");
 investTrueOrFalse= kbReader.nextBoolean();
 j++;
    }
  
    
    
    
     //j = kbReader.nextInt();
    // String addedStock = stockList.get(j);

    
      //   investorList.add(addedStock);
    
 //System.out.println("Would you like to invest in any more stocks? (true or false)");
 //investTrueOrFalse= kbReader.nextBoolean();
    
    
}
System.out.println("Okay, Lets see your stock list");
float divider = 0;
//int stockRisk=0;
for(int i = 0; i < investorList.size(); i++) {  
    System.out.print(investorList.get(i));
    System.out.println("\n ");
    String riskStringHelper = investorList.get(i);
    riskMan = riskStringHelper.charAt(riskStringHelper.length()-1);
    stockRisk = riskStringHelper.charAt(riskStringHelper.length()-1);
    riskHelper += Integer.parseInt(String.valueOf(riskMan));
    //float riskOfficial = riskHelper/i;
    //System.out.println(riskOfficial);
    // investorList.get(i);
    divider++;
} 
float riskOfficial = riskHelper/divider;
System.out.println("Your portfolio risk is " + riskOfficial);

for( int p = 0; p < investorList.size(); p++){
    String tempHelperString = investorList.get(p); 
    ///stockTicker = tempHelperString.next(",");
   /* String stockTicker;
*String stockName;
*float stockPrice;
*int stockRisk;
**/
Scanner input = new Scanner(tempHelperString);
  input.useDelimiter(",");
  while(input.hasNext()){
    stockTicker = input.next();
    stockName = input.next();
    stockPrice = input.nextDouble();
    double marketCap = input.nextDouble();
    String industry = input.next();
    stockRisk = input.nextInt();
    stockObject.add(new portfolioStocks(stockTicker, stockName, stockPrice, stockRisk));
  }



    //investorList.get(p) = tempHelperString; 
    //portfolioStocks portfolioStock = new portfolioStocks(stockTicker, stockName, stockPrice, stockRisk);
    //stockObject.add(new portfolioStocks(stockTicker, stockName, stockPrice, stockRisk));
}
        }
}

