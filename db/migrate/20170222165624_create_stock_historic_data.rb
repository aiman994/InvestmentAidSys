class CreateStockHistoricData < ActiveRecord::Migration[5.0]
  def change
    create_table :stock_historic_data do |t|
      t.string :stock_tickers
      t.string :price_date
      t.float :price_close
      t.float :price_high
      t.float :price_low
      t.float :price_open
      t.float :volume

       t.timestamps null: false
    end
  end
end
