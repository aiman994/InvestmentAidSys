class UserController < ApplicationController
  def signup
  	 @user = User.new
  end

 def create
    @user= User.new(user_params)
  	@passworddigest =  BCrypt::Password.create @user.password_digest
  	@user.password_digest = @passworddigest

  	if @user.save
      log_in @user
  		render 'welcome/homepage', :notice => "Thank you for signing up ! login to continue" 
    else
      render 'signup'
    end
 end
 def show

 end

private    
  def user_params
        params.require(:user).permit(:userId,:userFname, :user_Cntct,:user_email, :password_digest)
  end
end
