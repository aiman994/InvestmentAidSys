class AnalyzerController < ApplicationController

  def centralAnalysis
  	@stdout4, @stdeerr4, @status4= Open3.capture3("python app/assets/pythonScripts/newScrapeSumm.py "+ params[:id])
    @stdout3, @stdeerr3, @status3= Open3.capture3("python app/assets/pythonScripts/fbscrape.py "+ params[:id])
    @stdout2, @stdeerr2, @status2= Open3.capture3("python app/assets/pythonScripts/bloombergs.py "+ params[:id])
      
  	@stdout, @stdeerr, status = Open3.capture3("python app/assets/pythonScripts/dataPull.py "+ params[:id] )
  	$ticker = params[:id]
    @stdout1, @stdeerr1, status1= Open3.capture3("python app/assets/pythonScripts/patternRecognition.py "+ params[:id] )

    if session[:PID] == nil
      @pid = Process.spawn("python app/assets/pythonScripts/twitter.py "+ params[:id])
      
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

    @tweets = TwitterStream.where("stock_name =?",  params[:id]).reverse
    @fb = FbStream.where("stock_name =?", params[:id]).reverse
    @bloom= BloombergStream.where("companyNme =?", params[:id]).reverse
    @summ= CompanySummary.where("stock_tickers =?",  params[:id])
    @patfound= Prediction_Data.find_by_sql "SELECT stock_tickers,created_at FROM prediction_data WHERE stock_tickers= '"+ params[:id]+"' AND date(created_at)= '"+DateTime.now.beginning_of_day.to_s+"'"
  end
      

  def historic_data
        stock_data = StockHistoricData.where("stock_tickers =?", $ticker)
        prediction = Prediction_Data.where("stock_tickers =?", $ticker)
        
        File.open("data.json", "w") do |f|
           f.write(stock_data.to_json)
        end
        
        File.open("predict.json", "w") do |f|
           f.write(prediction.to_json)
        end
         render json: {"stock" => stock_data, 'prediction' => prediction}.to_json #convert into json format
      
  end


  def refresh_tweets
    
  end
end
