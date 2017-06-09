class User < ApplicationRecord
    has_secure_password
    EMAIL_REGEX = /[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}/i
    validates :user_email, :presence => true, :uniqueness => true, :format => EMAIL_REGEX
	#validates_length_of :password, :on => :create
end
