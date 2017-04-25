<link rel="stylesheet" href="/assets/css/session.scss">
<link rel="stylesheet" href="/assets/css/bootstrap-theme.min.css">
<link rel="stylesheet" href="/assets/css/bootstrap.min.css">
<head> <div><nav class="navbar navbar-inverse navbar-fixed-top">
        <a class="navbar-brand" href="#">Investment Aid System</a>
        <ul class="nav navbar-nav">
            <li ><a href="/views/welcome/homepage.html">Home</a></li>
            <li class="active"><a href="/views/applicaton/company.html">Companies</a></li>
            <li><a href="/views/viewer/news.html">News</a></li>
            <li ><a href="/views/welcome/about.html">About</a></li>
            <li><a href="/views/session/login.html">Login</a></li>
          </ul>

        </nav>
    </div>
</head>
<br>
<br>
<h1>Viewer#company</h1>
<%= form_tag(companies_path, :method => "get", id: "search-form") do %>
    <%= text_field_tag :search, params[:search], placeholder: "Search Companies" %>
    <%= submit_tag "Search", :name => nil, :controller => "viewer", :action => "list"%>
<% end %>

<% if @company.blank? %>
  <h4>There are no company containing the term <%= params[:search] %>.</h4>
<% end %>

<%= will_paginate @company %>
<table style="width: 80%; marginLeft:30px;">                         
  <tr style="height: 50px">
    <th>    </th>
    <th>    </th> 
    <th>    </th>     
    <th>No. </th> 
    <th>    </th>                     
    <th>Company Name</th>
    <th> Company Tickers  </th> 
    
  </tr>
    <% @company.each do |company|  %> 
  <tr>
    <td>    </td>
    <td>    </td>
    <td>   </td>
    <td><%= company.id %></td>
    <td>   </td> 
    <td><%= company.company_name %></td>
    <td><a href="/views/analyzer/centralAnalysis/<%= company.stock_tickers%>"> <%= company.stock_tickers%></a></td>
  </tr>

<% end %>                  
</table>               

