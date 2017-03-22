class CreateUsers < ActiveRecord::Migration[5.0]
  def change
    create_table :users do |t|
      t.integer :userId
      t.string :userFname
      t.string :password_digest
      t.string :user_Cntct
      t.string :user_email

<<<<<<< HEAD
      remove_column :users, :created_at
=======
      t.timestamps
>>>>>>> b5b8d16e79fff0e954da458cad9af177739ebb67
    end
  end
end
