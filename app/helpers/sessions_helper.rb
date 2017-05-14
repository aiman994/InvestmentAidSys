

module SessionsHelper
  def log_in(user)
    session[:user_id] = user.id
  end
   def current_user
    @current_user ||= User.find_by(id: session[:user_id])
  end

  def logged_in?
    !current_user.nil?
  end

   def log_out
    session.delete(:user_id)
    @current_user = nil
  end

  def process_id (id)
  	session[:PID] = id
  end

  def pid?
  	!session[:PID] = nil
  end

  def deletePid
  	session.delete(:PID)
  end

  def current_tick(tick)
      session[:ticker]=tick
  end
end
