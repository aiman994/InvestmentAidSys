class SessionController < ApplicationController
skip_before_filter  :verify_authenticity_token
    
    def login
      
    end

    def new
       
    end

    def create 
         user = User.find_by(user_email: params[:session][:user_email])
        if user && user.authenticate(params[:session][:password_digest])
            log_in user
            redirect_to root_path, :notice => 'Logged in successfully'
        else
            flash.now[:danger] = 'Invalid email/password combination'
            redirect_to root_path, :notice => "Tracker Disabled!"
            #render 'login'
        end
    end
    

    def login_param
         params.require(:login).permit(:user_email, :password_digest)
    end
    
    def destroy
        log_out
        redirect_to root_path
    end
end
