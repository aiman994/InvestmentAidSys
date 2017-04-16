class Changepredictdatacolumntype < ActiveRecord::Migration[5.0]
  def change
  	 change_table :prediction_data do |t|
      t.change :updated_at, :string
    end
  end
end
