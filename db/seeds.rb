# This file should contain all the record creation needed to seed the database with its default values.
# The data can then be loaded with the rails db:seed command (or created alongside the database with db:setup).
#
# Examples:
#
#   movies = Movie.create([{ name: 'Star Wars' }, { name: 'Lord of the Rings' }])
#   Character.create(name: 'Luke', movie: movies.first)
require 'user'

user = User.create([{userId: '17' ,userFname:'Aiman Aqilah', password_digest: User.digest('17'), user_Cntct:'0172256125', user_email:'aimanaqilahazmi@gmail.com'},{userId: '18' , userFname:'Aiman Afiqah', password_digest: User.digest('18'), user_Cntct:'0112345678', user_email:'aimanaafiqahazmi@gmail.com'}])



#table Lecturer

