class CompaniesController < ApplicationController

	def list
		if params[:search]
		   @company = Company.search(params[:search])
		else
		   @company = Company.all
		   @company = Company.paginate(:page => params[:page], :per_page => 30)
		end
	end
	def index
		
	end
end
