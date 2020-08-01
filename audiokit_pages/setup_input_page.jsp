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
java.sql.Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/audiokit","root","31@dec2019"); 
Statement st= con.createStatement(); 
 Connection connection = null;
 Statement statement = null;
 ResultSet resultSet = null;
 ResultSet resultSet_edit = null; 
 %>    
 
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Setup Device</title>
<script>
function f1()
{
document.setup_input.target ='setup_bottom_left_frame';
document.setup_input.search_by_phone_no_var.value="No";
document.setup_input.serach_by_phone_no_txt.value="";
document.setup_input.action="list_setup_device.jsp";
document.setup_input.submit();
}

function f2()
{
 document.setup_input.target ='setup_bottom_right_frame';
 document.setup_input.action="setup_device.jsp";
 document.setup_input.submit();
}

function search_by_phone_no()
{
 document.setup_input.target ='setup_bottom_left_frame';
 document.setup_input.search_by_phone_no_var.value="Yes";
 document.setup_input.client_id.value=""; 
 document.setup_input.zone_region.value="";
 //alert( document.setup_input.serach_by_phone_no_txt.value);
 //alert( document.setup_input.search_by_phone_no_var.value); 
 document.setup_input.action="list_setup_device.jsp";
 document.setup_input.submit();
}

</script>
<style>
body {
  color: black;
  font-family: Calibri;
  font-size: 90%;
}

input {
  color: black;
  font-family: Calibri;
  font-size: 90%;
}
option {
  color: black;
  font-family: Calibri;
  font-size: 90%;
}

select {
  color: black;
  font-family: Calibri;
  font-size: 100%;
}
</style>
</head>
<body style="font-size:15px">
<font style='font-family="Calibri"' >
<form action="" name="setup_input" >
<input type="hidden" name="search_by_phone_no_var">
<h3> Setup Device Details </h3>
<table border="0"  style="height: 300px;">
<tr> 
<td><label for="id1">Select Clients :</label></td>
<td>
<SELECT NAME="client_id" style="width:150px;">
<option value="" selected>All Clients</option>
<%
 try{
  statement=con.createStatement();
  String sql ="SELECT client_id,client_name FROM client_dtls where is_active='Y'";
  resultSet = statement.executeQuery(sql);
 while(resultSet.next()){
 %>
<option value="<%=resultSet.getString("client_id")%>"><%=resultSet.getString("client_name")%></option>
<%
}
 connection.close();
 } catch (Exception e) {
 e.printStackTrace();
 }
%>
</SELECT>
</td>
</tr>
<tr>
<td><label for="id2">Select Zones/Regions :</label></td>
<td> 
 <select name="zone_region" style="width: 150px;">
  <option value="" selected>All Zones/Region</option>
<%
 try{
  statement=con.createStatement();
  String sql ="SELECT zone_id,zone_name FROM device_zones_regions";
  resultSet = statement.executeQuery(sql);
 while(resultSet.next()){
 %>
<option value="<%=resultSet.getString("zone_id")%>"><%=resultSet.getString("zone_name")%></option>
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
<td>
</td>
<td>
<b> OR </b> 
</td>
</tr>
<tr>
<td>
<input type="button" name="serach_by_phone_no" value="Search By Phone No"  onclick="search_by_phone_no()">
</td>  
<td> 
   <input type="text" name="serach_by_phone_no_txt" value="" >     
</td>
</tr>
<tr>
<td>   
 <input type="button" name="Get_List" value="Get List" onclick="f1()">
</td>
<td>    
   <input type="button" name="add_new_device" value="Add New Device" onclick="f2()" >
</td>
 </tr>
   </table>   
  </form>
  </font>
</body>
</html>