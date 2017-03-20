class CreateCompanyTable < ActiveRecord::Migration[5.0]
  def change
    create_table :company_tables do |t|
    	t.string :company_name
    	t.string :stock_tickers
      	t.string :icompany_sector
    	t.string :company_industry
      	
      	t.timestamps null: false
    end
  end
end
