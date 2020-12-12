
/**
 * Write a description of class personClass here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
import java.util.Random;

public class portfolioStocks
{
   
    private boolean ox;
    private int y1;
    String stockTicker;
    String stockName;
    double stockPrice;
    int stockRisk;

    public portfolioStocks(String stockTicker, String stockName, double stockPrice, int stockRisk)
    {
        this.stockTicker = stockTicker;
        this.stockName = stockName;
        this.stockPrice = stockPrice; 
        this.stockRisk = stockRisk;
       
        
        
    }

   
    
    /**
     * 
     * 
     * 
     */
    public double stockPriceFluctuation(double stockPrice, int stockRisk)
    {
        
        if( stockRisk == 1){
            Random ran = new Random();
            int random = ran.nextInt(30)+1;
            int v = ran.nextInt(1) + 1;
            double stockHelper = random/100;
            double stockHelper1 = stockHelper * stockPrice;
            //int random = 
            if(v == 1){
            stockPrice = stockPrice + stockHelper1;
        }
         if(v == 2){
            stockPrice = stockPrice - stockHelper1;
        }
        }
        
        if( stockRisk == 2){
            
            
              Random ran = new Random();
            int random = ran.nextInt(60)+1;
            int v = ran.nextInt(1) + 1;
             double stockHelper = random/100;
            double stockHelper1 = stockHelper * stockPrice;
            //int random = 
            if(v == 1){
            stockPrice = stockPrice + stockHelper1;
        }
         if(v == 2){
            stockPrice = stockPrice - stockHelper1;
        }
        
            
        }
        
        if( stockRisk == 3){
              Random ran = new Random();
            int random = ran.nextInt(90)+1;
            int v = ran.nextInt(1) + 1;
             double stockHelper = random/100;
            double stockHelper1 = stockHelper * stockPrice;
            //int random = 
             if(v == 1){
            stockPrice = stockPrice + stockHelper1;
        }
         if(v == 2){
            stockPrice = stockPrice - stockHelper1;
        }
        
            
        }
        
        return stockPrice;
        
    }
}
