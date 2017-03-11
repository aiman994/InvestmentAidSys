class AnalyzerController < ApplicationController
  def centralAnalysis
  end
    
     def for_graph
        stock_data = StockHistoricData.all
        File.open("data.json", "w") do |f|
           f.write(stock_data.to_json)
        end
        
        render json: stock_data #convert into json format
     
    end
end
