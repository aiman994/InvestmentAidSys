class WelcomeController < ApplicationController   
    skip_before_filter :verify_authenticity_token, :only => :create
    def homepage
    	pid=Process.spawn("python app/assets/pythonScripts/twitter.py")
    end


    def about
        
        
    end
    
    
    
end