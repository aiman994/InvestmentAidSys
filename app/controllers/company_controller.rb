class CompanyController < ApplicationController
  def index
 	 		@comp = Company.all
 	 		@comp = Company.paginate(:page => params[:page], :per_page => 30)
 	 		if session[:PID] != nil
 	 			begin 
	 	 			Process.kill "TERM", session[:PID]
	      			deletePid
	      		rescue Errno::ESRCH
  					false
  					deletePid
  				end
      		end
	end

	def show
		
		if params[:search]
 	 		@companies = Company.search(params[:search])
  		else
  			@compaies=nil
  			@company= Company.all
		end

		@company = Company.paginate(:page => params[:page], :per_page => 30)
			if session[:PID] != nil
 	 			Process.kill "TERM", session[:PID]
      			deletePid
      		end
    end


	def create
	end


	def params_company
		params.require(:companies).permit(:search)
	end
end
