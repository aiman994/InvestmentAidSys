class CreatePredictionData < ActiveRecord::Migration[5.0]
  def change
    create_table :prediction_data,force: true do |t|
    		  t.string :stock_tickers
		      t.float :price_close
		      t.float :percentChange
		      t.float :predicted_price
       t.timestamps null: false
    end
  end
end
