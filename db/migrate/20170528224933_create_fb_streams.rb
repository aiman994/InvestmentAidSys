class CreateFbStreams < ActiveRecord::Migration[5.0]
  def change
    create_table :fb_streams do |t|
    	t.string :stock_name
	    t.string :fb_user
	    t.string :post
	    t.string :pic_url
	    t.string :posts_url
	    t.string :time_posted
      t.timestamps
    end
  end
end
