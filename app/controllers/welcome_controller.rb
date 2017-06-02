class WelcomeController < ApplicationController   
   # skip_before_filter :verify_authenticity_token, :only => :create
    def homepage
    	#@stdout, stdeerr, status = Open3.capture3("python app/assets/pythonScripts/industryScrape.py")
    	#pid = Process.spawn("python app/assets/pythonScripts/twitter.py ")
    end

    def about
        
        
    end
    
end