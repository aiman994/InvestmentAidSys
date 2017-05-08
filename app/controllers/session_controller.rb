class SessionController < ApplicationController
skip_before_filter  :verify_authenticity_token
    
    def login
      
    end

    def new
       
    end

    def create 
         user = User.find_by(user_email: params[:session][:user_email])
        if user && user.authenticate(params[:session][:password_digest])
            session[:user_id] = user.userFname
            render 'welcome/homepage' ,:notice => "Logged in!!"
        else
            render 'welcome/about',:notice => "sorry unknown combination of email and password"
        end
    end
    

    def login_param
         params.require(:login).permit(:user_email, :password_digest)
    end
    
    def destroy
        session[:user_id] = nil
        flash[:success] = "You have logged out"
        redirect_to root_path
    end
end
