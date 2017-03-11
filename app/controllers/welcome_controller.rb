class WelcomeController < ApplicationController   
    
    def homepage

    end


    def about
        
        #@stock_data = StockHistoricData.all
        #render json: @stock_data #convert into json format
        #@data = stock_data.to_json
        
    end
    
    def for_graph
        stock_data = StockHistoricData.all
        File.open("data.json", "w") do |f|
           f.write(stock_data.to_json)
        end
        
        render json: stock_data #convert into json format
     
    end
    
    
end