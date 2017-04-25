class SessionController < ApplicationController
skip_before_filter  :verify_authenticity_token 
    
    def login
       
    end

    def new
        
    end
    def create 
        user = User.find_by(user_email: params[:session][:user_email])
        if user && user.authenticate(params[:session][:password_digest])
            flash[:success] = "You have successfully logged in"
            log_in user
            redirect_to 'welcome/homepage'
        else
            flash.now[:danger] = 'Invalid email/password combination' # Not quite right!
            render 'new'
        end
    end
    

    def login_param
         params.require(:login).permit(:user_email, :password_digest)
    end
    
    def destroy
        session[:user_email] = nil
        flash[:success] = "You have logged out"
        redirect_to root_path
    end
end
