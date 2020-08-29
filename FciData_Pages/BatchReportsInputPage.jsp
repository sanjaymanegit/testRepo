<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>   
    
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">


<%@page import="java.sql.DriverManager"%>
<%@page import="java.sql.ResultSet"%>
<%@page import="java.sql.Statement"%>
<%@page import="java.sql.Connection"%>
<%@page import ="java.sql.*" %>
<%@page import ="javax.sql.*" %>

<%
Class.forName("com.mysql.jdbc.Driver"); 
java.sql.Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/fci","root","31@dec2019"); 
Statement st= con.createStatement(); 
 Connection connection = null;
 Statement statement = null;
 ResultSet resultSet = null;
 %> 


<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<link rel="stylesheet" type="text/css" href="jquery.datetimepicker.css"/>
<title>Insert title here</title>
<link rel="stylesheet" href="//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">
<link rel="stylesheet" href="/resources/demos/style.css">
<script src="jquery-1.12.4.js"></script>
<script src="jquery-ui.js"></script>
  <script>
  jQuery(document).ready(function () {
      'use strict';

      jQuery('#filter-date, #to_date').datepicker();
  });
  </script>
  <script>
  
  function f_get_batch_list()
  {
	  var x =document.inputs_frm.device_id.value;	  	  
	  if(x == "")
		 {
				  alert ("Please select device_id !!!");	
				  return false;
			
		 }
		  else
		   {
			  document.inputs_frm.target ="rightbottomframe"; 
			  document.inputs_frm.action="batch_list.jsp";
			  document.inputs_frm.method="post";
			  document.inputs_frm.submit();
			  return true;			  
			}
  }
  
  
  function dev_on_change() 
  {
   
      document.inputs_frm.target ="leftbottomframe";      
	  document.inputs_frm.action="BatchReportsInputPage.jsp";
	  document.inputs_frm.work_order_ids.selectcted.value=document.inputs_frm.work_order_ids.value;	  
	  document.inputs_frm.device_id.selectcted.value=document.inputs_frm.device_id.value;	  
	  document.inputs_frm.method="post";
	  document.inputs_frm.submit();	  
  }
  </script>
  
<style>
body {
  color: black;
  font-family: Verdana, Geneva, sans-serif;
  font-size: 80%;
}

label {
  color: blue;
  font-family: Verdana, Geneva, sans-serif;
  font-size: 90%;
}

option {
  color: black;
  font-family: Verdana, Geneva, sans-serif;
  font-size: 80%;
}

select {
  color: black;
  font-family: Verdana, Geneva, sans-serif;
  font-size: 100%;
}
</style>
  
</head>
<body>
<label for="note"> Search Batch. </label>
<form name="inputs_frm" >
<%
String rolename = request.getParameter("role_name");
String wo_id = request.getParameter("work_order_ids");
String username = request.getParameter("username");
//out.println(" user_name :"+username);
//out.println(" work_order_ids :"+wo_id);
out.println("<input type=hidden name=username value="+username+">");
out.println("<input type=hidden name=role_name value="+rolename+">");
%>
<table border="0" style="height: 300px;" >
<tr>
<td><label for="device_id"> Device Id: </label></td>
<td>
<select name="device_id" style="width: 175px; height: 30px;" >   
 <%
 try{ 
 statement=con.createStatement();  
 String sql ="SELECT d.device_id,d.device_id_str FROM device_dtls d";
 resultSet = statement.executeQuery(sql);
 while(resultSet.next()){
 %>
<option style="width: 175px; height: 30px;" value="<%=resultSet.getString("device_id_str") %>"><%=resultSet.getString("device_id_str") %></option>
<%
}
 connection.close();
 } catch (Exception e) {
 e.printStackTrace();
 }
%>
 </select>
</td>
</tr>
<tr>
<td><label for="id"> From Date: </label></td>
<td><input name="from_date_val" id="filter-date" value="08/05/2020" style="width: 175px; height: 30px;" ></td>
</tr>
<tr>
<td><label for="name">To Date: </label></td>
<td><input name="to_date_val" id="to_date" maxlength="50" name="name" value="12/31/2020" style="width: 175px; height: 30px;"></td>
</tr>
<tr>
<td></td>
<td align="right">
<input type="button" name="get_batch_list" value="Get List" onclick="f_get_batch_list()">
&nbsp;&nbsp;&nbsp;
<input type="reset" name="rest_get_batch_list" value="Reset">
</td>
</tr>
</tbody>
</table>
</form>
</body>
</html>