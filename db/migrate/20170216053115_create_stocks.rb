class CreateStocks < ActiveRecord::Migration[5.0]
  def change
    create_table :stocks,force: true do |t|

    
    t.timestamps null: false
    end
  end
end
