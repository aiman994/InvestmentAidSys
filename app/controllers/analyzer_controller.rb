class AnalyzerController < ApplicationController
  def centralAnalysis
  	
  	@stdout, stdeerr, status = Open3.capture3("python app/assets/pythonScripts/technicalAnalysis.py " + params[:id] )
  	@ticker = params[:id]
    @stdout1, @stdeerr1, status1= Open3.capture3("python app/assets/pythonScripts/patternRecognition.py")
    
  end
    
   	def historic_data

        stock_data = StockHistoricData.all
        File.open("data.json", "w") do |f|
           f.write(stock_data.to_json)
        end
        render json: stock_data #convert into json format
    end

    def predicted_data
        prediction = Prediction_Data.where("stock_tickers =?", params[:tick])
        File.open("predict.json", "w") do |f|
           f.write(prediction.to_json)
        end
        render json: prediction #convert into json format
        puts $id
    end
end
