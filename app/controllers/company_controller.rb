class CompanyController < ApplicationController
  def index
 	 		@comp = Company.all
 	 		@comp = Company.paginate(:page => params[:page], :per_page => 30)
	end

	def show
		
		if params[:search]
 	 		@companies = Company.search(params[:search])
  		else
  			@compaies=nil
  			@company= Company.all
		end
		@company = Company.paginate(:page => params[:page], :per_page => 30)
		#@comp = Company.paginate(:page => params[:page], :per_page => 30)
	end

	def create
	end


	def params_company
		params.require(:companies).permit(:search)
	end
end
