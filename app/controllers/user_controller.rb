class UserController < ApplicationController
  def signup
  end
 def new
        @users= User.all
 end
    
  def user_params
        params.require(:user).permit(:userId, :password_digest)
  end
end
