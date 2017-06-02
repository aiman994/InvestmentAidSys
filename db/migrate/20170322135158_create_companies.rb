class CreateCompanies < ActiveRecord::Migration[5.0]
  def change
    create_table :company,force: true do |t|
    	t.string :company_name
    	t.string :stock_tickers
      	t.string :company_sector
    	t.string :company_industry
      	
      	t.timestamps null: false
      	
    end
  end
end
