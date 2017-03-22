class CreateStocks < ActiveRecord::Migration[5.0]
  def change
    create_table :stocks do |t|

<<<<<<< HEAD
    
    t.timestamps null: false
=======
      t.timestamps
>>>>>>> b5b8d16e79fff0e954da458cad9af177739ebb67
    end
  end
end
