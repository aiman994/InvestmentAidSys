class AnalyzerController < ApplicationController
  def centralAnalysis
  	
  	@stdout, stdeerr, status = Open3.capture3("python app/assets/pythonScripts/technicalAnalysis.py " + params[:id] )
  	$ticker = params[:id]
    @stdout1, @stdeerr1, status1= Open3.capture3("python app/assets/pythonScripts/patternRecognition.py")
    @tweets = TwitterStream.all
    
  end
      def historic_data

        stock_data = StockHistoricData.all
        prediction = Prediction_Data.where("stock_tickers =?", $ticker)
        
        File.open("data.json", "w") do |f|
           f.write(stock_data.to_json)
        end
        
        File.open("predict.json", "w") do |f|
           f.write(prediction.to_json)
        end
        
        render json: {'stock' => stock_data, 'prediction' => prediction}.to_json #convert into json format


      end
end
