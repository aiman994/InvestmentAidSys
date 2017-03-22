class AnalyzerController < ApplicationController
  def centralAnalysis
  	#@p = StockHistoricData.find_by_id(params[:id])
  	@stdout, stdeerr, status = Open3.capture3("python app/assets/pythonScripts/technicalAnalysis.py " + params[:id] )
  	@ticker = params[:id]
  	 
  end
    
   	def for_graph

        stock_data = StockHistoricData.all
        File.open("data.json", "w") do |f|
           f.write(stock_data.to_json)
        end
        render json: stock_data #convert into json format
    end
end
