class WelcomeController < ApplicationController   
   # skip_before_filter :verify_authenticity_token, :only => :create
    def homepage
    	@bloom= BloombergStream.last(3)
    end

    def about
        
        
    end
    
end