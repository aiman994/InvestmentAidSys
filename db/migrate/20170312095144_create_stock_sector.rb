class CreateStockSector < ActiveRecord::Migration[5.0]
  def change
    create_table :stock_sectors,force: true do |t|
      t.string :sectors_name
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
    end
  end
end
