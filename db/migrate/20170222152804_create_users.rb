class CreateUsers < ActiveRecord::Migration[5.0]
  def change
    create_table :users,force: true do |t|
      t.integer :userId
      t.string :userFname
      t.string :password_digest
      t.string :user_Cntct
      t.string :user_email
    end
  end
end
