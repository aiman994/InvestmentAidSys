class SessionController < ApplicationController
  def login
  end
    def new
        
    end
    def create 
        
        user = User.find_by(userId: params[:session][:userId].downcase)
        
        if user && user.authenticate(params[:session][:password_digest])

         #flash[:success] = "You have successfully logged in"
         #   log_in Login
            
           redirect_to sessionselection_path, :notice => "You have successfully logged in"

        else

           redirect_to root_path, :notice => "There was something wrong with your login information"

        end
       

    end
    
     def login_param
         params.require(:login).permit(:userId, :password_digest)
   end
    
    def destroy
        session[:userId] = nil

        flash[:success] = "You have logged out"

        redirect_to root_path

    end
end
