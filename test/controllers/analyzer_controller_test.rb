require 'test_helper'

class AnalyzerControllerTest < ActionDispatch::IntegrationTest
  test "should get centralAnalysis" do
    get analyzer_centralAnalysis_url
    assert_response :success
  end

end
