class StockIndustry < ActiveRecord::Migration[5.0]
  def change
  	create_table :stock_industry do |t|
      t.string :industry_name
      t.string :industry_sector
      t.float :dayprice_change
      t.float :market_cap
      t.float :p_earning
      t.float :returnEquity
      t.float :div_yield
      t.float :longTermDebttoEquity
      t.float :priceTobook
      t.float :netProfitMargin
      t.float :priceToFreecashFlow
        
    t.timestamps null: false
    remove_column :users, :created_at
	end
  end
end
