class Addcolumntofb < ActiveRecord::Migration[5.0]
  def change
  	add_column :fb_streams, :polarity, :string
  	add_column :fb_streams, :subjectivity, :string
  end
end
