class WelcomeController < ApplicationController   
    skip_before_filter :verify_authenticity_token, :only => :create
    def homepage

    end


    def about
        
        
    end
    
    
    
end