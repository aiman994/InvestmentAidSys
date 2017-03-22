require 'test_helper'

class ApplicationControllerTest < ActionDispatch::IntegrationTest
  test "should get news" do
    get application_news_url
    assert_response :success
  end

end
