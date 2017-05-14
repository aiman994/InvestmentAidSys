class AnalyzerController < ApplicationController
  def centralAnalysis
  	
  	@stdout, stdeerr, status = Open3.capture3("python app/assets/pythonScripts/technicalAnalysis.py " + params[:id] )
  	$ticker = params[:id]
    @stdout1, @stdeerr1, status1= Open3.capture3("python app/assets/pythonScripts/patternRecognition.py")
    

    if session[:PID] == nil
      @pid = Process.spawn("python app/assets/pythonScripts/twitter.py "+ params[:id]  )
      process_id @pid
      current_tick $ticker
    else 
      if  session[:ticker] != params[:id]
        begin 
            Process.kill "TERM", session[:PID]
        rescue Errno::ESRCH
            false
        end
         deletePid
      end

    end
    @tweets = TwitterStream.where("stock_name =?", $ticker).order("updated_at DESC")
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


  def refresh_tweets
    
  end
end
