class Changepredictdatacolumntype < ActiveRecord::Migration[5.0]
  def change
  	 change_table :prediction_data,force: true do |t|
      t.change :updated_at, :string
    end
  end
end
