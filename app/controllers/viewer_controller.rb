class ViewerController < ApplicationController

  def list

  	 @company = Company.all
  	 @company = Company.paginate(:page => params[:page], :per_page => 30)
  end

end
