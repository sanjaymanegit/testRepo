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
<title>Insert title here</title>
<script>
function f1()
{
document.reportInput.target = 'bottomframe';	
document.reportInput.action="List.jsp";
document.reportInput.submit();
}

function client_onchange()
{  
  document.reportInput.target = 'topframe';	  
  document.reportInput.client_name.selectcted.value=document.reportInput.client_name.value;
  document.reportInput.action="ReportsInputPage.jsp";
  document.reportInput.submit();	
}

function zone_onchange()
{ 
 document.reportInput.client_name.selectcted.value=document.reportInput.client_name.value;
 document.reportInput.zone.selected.value=document.reportInput.zone.value;
  document.reportInput.action="ReportsInputPage.jsp";
  document.reportInput.submit();	
}

function state_onchange()
{ 
 document.reportInput.client_name.selectcted.value=document.reportInput.client_name.value;
 document.reportInput.zone.selected.value=document.reportInput.zone.value;
 document.reportInput.state.selected.value=document.reportInput.state.value;
 
  document.reportInput.action="ReportsInputPage.jsp";
  document.reportInput.submit();	
}

function city_onchange()
{ 
 document.reportInput.city.selectcted.value=document.reportInput.city.value;
 document.reportInput.client_name.selectcted.value=document.reportInput.client_name.value;
 document.reportInput.zone.selected.value=document.reportInput.zone.value;
 document.reportInput.state.selected.value=document.reportInput.state.value; 
 document.reportInput.action="ReportsInputPage.jsp";
 document.reportInput.submit();	
}

function search_by_phone_no()
{
 document.reportInput.target = 'bottomframe';
 document.reportInput.search_by_phone_no_var.value="Yes";
 document.reportInput.client_name.value=""; 
 document.reportInput.zone.value="";
 document.reportInput.state.value="";
 document.reportInput.city.value=""; 
 document.reportInput.action="List.jsp";
 document.reportInput.submit();
}


function search_by_panel_id()
{
 document.reportInput.target = 'bottomframe';
 document.reportInput.search_by_panel_id_flg.value="Yes";
 document.reportInput.client_name.value=""; 
 document.reportInput.zone.value="";
 document.reportInput.state.value="";
 document.reportInput.city.value=""; 
 document.reportInput.action="List.jsp";
 document.reportInput.submit();
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
<form action="" name="reportInput" >
<h3> Online/Offline List </h3>
<input type="hidden" name="search_by_phone_no_var">
<input type="hidden" name="search_by_panel_id_flg">
<%

//String zone_region_id=request.getParameter("zone_region");
String client_id=request.getParameter("client_name");
String zone_name=request.getParameter("zone");
String state_name=request.getParameter("state");
//String search_by_phone_no_var=request.getParameter("search_by_phone_no_var");
//String serach_by_phone_no_txt=request.getParameter("serach_by_phone_no_txt");
String condition_str= " 1=1";
String condition_state= " 1=1";
String condition_city= " 1=1";


//out.println("client_id :"+client_id);
/*if(search_by_phone_no_var != null && !search_by_phone_no_var.trim().isEmpty())
{
 if(serach_by_phone_no_txt.length() > 0 )
	{
	 condition_str =condition_str + " AND  A.DEV_ID='"+serach_by_phone_no_txt+"'";  
	}
}
*/

if(client_id != null && !client_id.trim().isEmpty())
{
	condition_str = " client_id ='"+client_id+"'";  
}

if(zone_name != null && !zone_name.trim().isEmpty())
{

	condition_state ="  zone_name='"+zone_name+"'";  
}

if(state_name != null && !state_name.trim().isEmpty())
{

	condition_city ="  State_name='"+state_name+"'";  
}


//out.println("condition_str :"+condition_str);

%>



<table border="0" style="height: 300px;">
<tr>
<td>
<label for="id1"> Client Name :</label>
</td>
<td>
<SELECT NAME="client_name" style="width: 150px;" onchange="client_onchange()">
<option value="" selected>All Clients</option>
<%
 try{
  statement=con.createStatement();
  String sql ="SELECT client_id,client_name FROM client_dtls where is_active='Y' ";
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
<td>
<label for="id2">Select Zone :</label>
</td>
<td>
<select name="zone" style="width: 150px;" onchange="zone_onchange()">
  <option value="" selected>All Zones/Regions</option>
<%
 try{
  statement=con.createStatement();
  String sql ="SELECT distinct zone_id,zone_name FROM client_zons_vw where "+condition_str;
  resultSet = statement.executeQuery(sql);
 while(resultSet.next()){
 %>
<option value="<%=resultSet.getString("zone_name")%>"><%=resultSet.getString("zone_name")%></option>
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
<label for="id3">Select State :</label>
</td>
<td>
<select name="state" style="width: 150px;" onchange="state_onchange()">
<option value="" selected> All States</option>
<%
 try{
  statement=con.createStatement();
  String sql ="SELECT state_id,state_name FROM device_states where "+condition_state;
  resultSet = statement.executeQuery(sql);
 while(resultSet.next()){
 %>
<option value="<%=resultSet.getString("state_name")%>"><%=resultSet.getString("state_name")%></option>
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
<label for="id4">Select City :</label>
</td>
<td>
<select name="city" style="width: 150px;" onchange="city_onchange()">
<option value="" selected> All Cities</option>
<%
 try{
  statement=con.createStatement();
  String sql ="SELECT city_id,city_name FROM device_city where "+condition_city;
  resultSet = statement.executeQuery(sql);
 while(resultSet.next()){
 %>
<option value="<%=resultSet.getString("city_name")%>"><%=resultSet.getString("city_name")%></option>
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
<label for="id5">Select Online/Offline :</label>
</td>
<td>  
 <input type="radio" name="status" value="Online" > Online  
  <input type="radio" name="status" value="Offline" > Offline <br>
  <input type="radio" name="status" value="" checked > Both(Online/Offline)
 </td>
 </tr>
 <tr>
 <td>
<label for="id6"><input type="button" name="serach_by_phone_no" value="Search By Phone No"  onclick="search_by_phone_no()"> :</label>
</td>
 <td> 
 <input type="text" name="serach_by_phone_no_txt" value="" >
 </td>
 </tr>
 <tr>
 <td>
<label for="id6"><input type="button" name="serach_by_panel_id" value="Search By Panel Id"  onclick="search_by_panel_id()"> :</label>
</td>
 <td> 
 <input type="text" name="serach_by_panel_id_txt" value="" >
 </td>
 </tr>
 <tr>
 <td>
 </td>
 <td>
 <input type="button" name="Get_List" value="Get List"  onclick="f1()">
 <input type="reset" name="reset_button" value="Reset">
</td> 
 </tr>
 </table> 
  </form>
  </font>
</body>
</html>