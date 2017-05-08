class Deletecolumnupdatedfromtwiitstream < ActiveRecord::Migration[5.0]
  def change
  	remove_column :twitter_streams, :updated_at
  end
end
