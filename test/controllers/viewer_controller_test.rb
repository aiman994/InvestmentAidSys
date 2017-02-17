require 'test_helper'

class ViewerControllerTest < ActionDispatch::IntegrationTest
  test "should get companies" do
    get viewer_companies_url
    assert_response :success
  end

end
