class Company < ApplicationRecord
		self.table_name = "company"
	def self.search(search)
		where("stock_tickers LIKE ?", "%#{search}%") 
		#where(["company_name LIKE ? OR stock_tickers LIKE ?", "%#{searchs}%", "%#{searchs}%"])
	end

end
