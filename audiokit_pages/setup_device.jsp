<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
    
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
     
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Setup Device Details </title>
<script> 
function add_device()
{
	document.cr_new_device.flag.value="add";
	document.cr_new_device.action="setup_device.jsp";
	document.cr_new_device.submit();
}
function save_device()
{	
	document.cr_new_device.flag.value="save";
	document.cr_new_device.action="setup_device.jsp";
	//alert(document.cr_new_device.client_id.value);
	document.cr_new_device.submit();
	
	
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
<form name="cr_new_device" >
<input type="hidden" Name="flag">
<font style='font-family="Calibri"'>
<%
String flag=request.getParameter("flag");
String client_id=request.getParameter("client_id");
String zone_region_id=request.getParameter("zone_region");
String state=request.getParameter("state");
String city=request.getParameter("city");
String phone_no_txt=request.getParameter("phone_no_txt");
String panel_id_text=request.getParameter("panel_id_text");
String address_txt=request.getParameter("address_txt");
String in_phone_no_1=request.getParameter("in_phone_no_1");
String in_phone_no_2=request.getParameter("in_phone_no_2");
String in_phone_no_3=request.getParameter("in_phone_no_3");
String in_phone_no_4=request.getParameter("in_phone_no_4");
String in_phone_no_5=request.getParameter("in_phone_no_5");
String in_phone_no_6=request.getParameter("in_phone_no_6");
String in_phone_no_7=request.getParameter("in_phone_no_7");
String in_phone_no_8=request.getParameter("in_phone_no_8");
String in_phone_no_9=request.getParameter("in_phone_no_9");
String in_phone_no_10=request.getParameter("in_phone_no_10");


//out.println("flag is :"+flag+" zone: "+zone+" area_subzone :"+area_subzone+" phone_no :"+phone_no_txt+" in_phone_no_txt :"+in_phone_no_txt+" address_txt  :"+address_txt); 


 try{
	  
 if (flag==null || flag.equals("add") )
 {
  out.println("<h2> Add New Device Details </h2>");
  %> 
  <table border="0" >
<tr>
<td width="40%">Client Name :</td>
<td width="40%"> <SELECT NAME="client_id" style="width: 150px;">
<option value="0">Select Client</option>
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
<td width="5%">
</td>
</tr>  
<tr>
<td >Zone/Region : </td>
<td >
<select name="zone_region" style="width: 150px;">
  <option value="">Select Zones/Region</option>
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
<td>
</td>
</tr>
<tr>
<td>State :</td>
<td>
<select name="state" style="width: 150px;">
<option value="" selected> Select State</option>
<%
 try{
  statement=con.createStatement();
  String sql ="SELECT state_id,state_name FROM device_states";
  resultSet = statement.executeQuery(sql);
 while(resultSet.next()){
 %>
<option value="<%=resultSet.getString("state_id")%>"><%=resultSet.getString("state_name")%></option>
<%
}
 connection.close();
 } catch (Exception e) {
 e.printStackTrace();
 }
%>
 </select>
</td>
<td>
</td>
</tr>
<tr>
<td>City :</td>
<td>
<select name="city" style="width: 150px;">
<option value="" selected> Select City</option>
<%
 try{
  statement=con.createStatement();
  String sql ="SELECT city_id,city_name FROM device_city";
  resultSet = statement.executeQuery(sql);
 while(resultSet.next()){
 %>
<option value="<%=resultSet.getString("city_id")%>"><%=resultSet.getString("city_name")%></option>
<%
}
 connection.close();
 } catch (Exception e) {
 e.printStackTrace();
 }
%>
 </select>
</td>
<td>
</td>
</tr>
<tr>
<td>*Phone No :</td>
<td><input type="text" name="phone_no_txt" style="width: 150px;" ></td>
<td>
</td>
</tr>
<tr >
<td valign="top">Panel ID :</td>
<td valign="top"><input type="text" name="panel_id_text" style="width: 150px;"></td>
<td>
</td>
</tr>
<tr>
<td valign="top">Address :</td>
<td valign="top">
<input type="text" name="address_txt"  maxlength="500" style="width: 150px;">
</td>
<td>
</td>
</tr>
<tr>
<tr>
<td valign="top">Ref. Incoming Phones :</td>
<td valign="top">
<select name="ref_incom_phones" style="width: 150px;">
<option value="" selected> Select Phone Nos.</option>
<%
 try{
  statement=con.createStatement();
  String sql ="SELECT distinct IN_PHONE_NO FROM vw_ref_phones";
  resultSet = statement.executeQuery(sql);
 while(resultSet.next()){
 %>
<option value="<%=resultSet.getString("IN_PHONE_NO")%>"><%=resultSet.getString("IN_PHONE_NO")%></option>
<%
}
 connection.close();
 } catch (Exception e) {
 e.printStackTrace();
 }
%>
 </select>
</td>
<td>
</td>
</tr>
<td>In-comming Phone (1):</td>
<td><input type="text" name="in_phone_no_1"   style="width: 150px;">  <input type="button" name="in_phone_no_1_bt" value="<<"  style="width: 35px;" onclick="document.cr_new_device.in_phone_no_1.value=document.cr_new_device.ref_incom_phones.value"></td>
<td>
</td>
</tr>
<tr>
<td>In-comming Phone (2):</td>
<td><input type="text" name="in_phone_no_2"   style="width: 150px;"> <input type="button" name="in_phone_no_2_bt" value="<<"  style="width: 35px;" onclick="document.cr_new_device.in_phone_no_2.value=document.cr_new_device.ref_incom_phones.value"></td>
<td>
</td>
</tr>
<tr>
<td>In-comming Phone (3):</td>
<td><input type="text" name="in_phone_no_3"   style="width: 150px;"> <input type="button" name="in_phone_no_3_bt" value="<<"  style="width: 35px;" onclick="document.cr_new_device.in_phone_no_3.value=document.cr_new_device.ref_incom_phones.value"></td>
<td>
</td>
</tr>
<tr>
<td>In-comming Phone (4):</td>
<td><input type="text" name="in_phone_no_4"   style="width: 150px;"> <input type="button" name="in_phone_no_4_bt" value="<<"  style="width: 35px;" onclick="document.cr_new_device.in_phone_no_4.value=document.cr_new_device.ref_incom_phones.value"></td>
<td>
</td>
</tr>
<tr>
<td>In-comming Phone (5):</td>
<td><input type="text" name="in_phone_no_5"   style="width: 150px;"> <input type="button" name="in_phone_no_5_bt" value="<<"  style="width: 35px;" onclick="document.cr_new_device.in_phone_no_5.value=document.cr_new_device.ref_incom_phones.value"></td>
<td>
</td>
</tr>
<tr>
<td>In-comming Phone (6):</td>
<td><input type="text" name="in_phone_no_6"   style="width: 150px;"> <input type="button" name="in_phone_no_6_bt" value="<<"  style="width: 35px;" onclick="document.cr_new_device.in_phone_no_6.value=document.cr_new_device.ref_incom_phones.value"></td>
<td>
</td>
</tr>
<tr>
<td>In-comming Phone (7):</td>
<td><input type="text" name="in_phone_no_7"   style="width: 150px;"> <input type="button" name="in_phone_no_7_bt" value="<<"  style="width: 35px;" onclick="document.cr_new_device.in_phone_no_7.value=document.cr_new_device.ref_incom_phones.value"></td>
<td>
</td>
</tr>
<tr>
<td>In-comming Phone (8):</td>
<td><input type="text" name="in_phone_no_8"   style="width: 150px;"> <input type="button" name="in_phone_no_8_bt" value="<<"  style="width: 35px;" onclick="document.cr_new_device.in_phone_no_8.value=document.cr_new_device.ref_incom_phones.value"></td>
<td>
</td>
</tr>
<tr>
<td>In-comming Phone (9):</td>
<td><input type="text" name="in_phone_no_9"   style="width: 150px;"> <input type="button" name="in_phone_no_9_bt" value="<<"  style="width: 35px;" onclick="document.cr_new_device.in_phone_no_9.value=document.cr_new_device.ref_incom_phones.value"></td>
<td>
</td>
</tr>
<tr>
<td>In-comming Phone (10):</td>
<td><input type="text" name="in_phone_no_10"  style="width: 150px;"> <input type="button" name="in_phone_no_10_bt" value="<<"  style="width: 35px;" onclick="document.cr_new_device.in_phone_no_10.value=document.cr_new_device.ref_incom_phones.value"></td>
<td>
</td>
</tr>
<tr>
<td></td>
<td></td>
<td>
</td>
</tr>
<tr>
<td></td>
<td></td>
<td>
</td>
</tr>
<tr>
<td></td>
<td></td>
<td>
</td>
</tr>
<tr>
<td></td>
<td></td>
<td>
</td>
</tr>
<tr>
<td>
<input type="button" Name"add_device" value="Add Device" onclick="add_device()">
&nbsp;&nbsp;
<input type="reset" Name"reset_device" value="Reset">
</td>
<td></td>
<td>
</td>
</tr>
</table>  
  <%  
 }	 
 if (flag.equals("add") && (phone_no_txt != ""))
 {	 

 //String sql ="INSERT INTO device_dtls (DEV_ID,ADDRESS,ZONE_REGION_ID,PANEL_ID,CLIENT_ID,CITY_ID,STATE_ID) VALUES('"+phone_no_txt+"','"+address_txt+"','"+zone_region_id+"','"+panel_id_text+"','"+client_id+"','"+city+"','"+state+"')";
	 
 String sql ="INSERT INTO device_dtls (DEV_ID,ADDRESS,ZONE_REGION_ID,PANEL_ID,CLIENT_ID,CITY_ID,STATE_ID,IN_PHONE_NO_1,IN_PHONE_NO_2,IN_PHONE_NO_3,IN_PHONE_NO_4,IN_PHONE_NO_5, IN_PHONE_NO_6,IN_PHONE_NO_7,IN_PHONE_NO_8,IN_PHONE_NO_9,IN_PHONE_NO_10,ui_update_status) VALUES('"+phone_no_txt+"','"+address_txt+"','"+zone_region_id+"','"+panel_id_text+"','"+client_id+"','"+city+"','"+state+"','"+in_phone_no_1+"','"+in_phone_no_2+"','"+in_phone_no_3+"','"+in_phone_no_4+"','"+in_phone_no_5+"','"+in_phone_no_6+"','"+in_phone_no_7+"','"+in_phone_no_8+"','"+in_phone_no_9+"','"+in_phone_no_10+"','UI_UPDATED')"; 
 out.println("sql add :"+sql);
 statement=con.createStatement(); 
 statement.executeUpdate(sql);
 out.println("Added Record Sccessfully !!!!!!");
 //out.println("<h2> Add New Device Details </h2>");
 connection.close();
 }
 else if (flag.equals("save") && (phone_no_txt != ""))
 {
	  client_id=request.getParameter("client_id");
	  zone_region_id=request.getParameter("zone_region");
	  state=request.getParameter("state");
	  city=request.getParameter("city");
	  phone_no_txt=request.getParameter("phone_no_txt");
	  panel_id_text=request.getParameter("panel_id_text");
	  address_txt=request.getParameter("address_txt");
	  in_phone_no_1=request.getParameter("in_phone_no_1");
	  in_phone_no_2=request.getParameter("in_phone_no_2");
	  in_phone_no_3=request.getParameter("in_phone_no_3");
	  in_phone_no_4=request.getParameter("in_phone_no_4");
	  in_phone_no_5=request.getParameter("in_phone_no_5");
	  in_phone_no_6=request.getParameter("in_phone_no_6");
	  in_phone_no_7=request.getParameter("in_phone_no_7");
	  in_phone_no_8=request.getParameter("in_phone_no_8");
	  in_phone_no_9=request.getParameter("in_phone_no_9");
	  in_phone_no_10=request.getParameter("in_phone_no_10");
	 //out.println("<h2>  in_phone_no_7 !!!</h2>"+in_phone_no_7);
 	 String sql ="UPDATE device_dtls SET client_id='"+client_id+"', zone_region_id='"+zone_region_id+"', city_id='"+city+"', state_id='"+state+"', PANEL_ID='"+panel_id_text+"', ADDRESS='"+address_txt+"' ,IN_PHONE_NO_2='"+in_phone_no_2+"', IN_PHONE_NO_1 = '"+in_phone_no_1+"', IN_PHONE_NO_2 = '"+in_phone_no_2+"', IN_PHONE_NO_3 = '"+in_phone_no_3+"', IN_PHONE_NO_4 = '"+in_phone_no_4+"', IN_PHONE_NO_5 = '"+in_phone_no_5+"', IN_PHONE_NO_6 = '"+in_phone_no_6+"', IN_PHONE_NO_7 = '"+in_phone_no_7+"', IN_PHONE_NO_8 = '"+in_phone_no_8+"', IN_PHONE_NO_9 = '"+in_phone_no_9+"', IN_PHONE_NO_10 = '"+in_phone_no_10+"', ui_update_status= 'UI_UPDATED'  WHERE DEV_ID='"+phone_no_txt+"'";
 	 //out.println("<h2>  sql sTRING </h2>"+sql);
	 statement=con.createStatement(); 
 	 statement.executeUpdate(sql); 	 
 	 out.println("<h2>  Saved Sucessfully !!!</h2>");
 	 connection.close(); 	 
 }
 else if (flag.equals("edit"))
 {
	 String edit_dev_id=request.getParameter("edit_radio");
	 out.println("<h2> Edit Device Details </h2>");
	 statement=con.createStatement();
	 String sql ="SELECT  DEV_ID ,IFNULL(state_id,0) as state_id ,ifnull(city_id,0) as city_id , client_id,ifnull(ZONE_REGION_ID,0) as  ZONE_REGION_ID, ADDRESS , PANEL_ID,IN_PHONE_NO_1 ,IN_PHONE_NO_2 ,IN_PHONE_NO_3 ,IN_PHONE_NO_4 ,IN_PHONE_NO_5 ,IN_PHONE_NO_6 ,IN_PHONE_NO_7 ,IN_PHONE_NO_8 ,IN_PHONE_NO_9 ,IN_PHONE_NO_10  FROM device_dtls where dev_id='"+edit_dev_id+"'"; 
	 resultSet_edit = statement.executeQuery(sql);
	 while(resultSet_edit.next()){
	%>	
<table border="0">
<tr>
<td width="40%">Client Name :</td>
<td width="50%"> <SELECT NAME="client_id" style="width: 150px;">
<option value="0">Select Client</option>
<%
 try{
 statement=con.createStatement();
 sql ="SELECT client_id,client_name FROM client_dtls where is_active='Y'";
 resultSet = statement.executeQuery(sql);
 while(resultSet.next()){
   if(!(resultSet.getString("client_id").equals(resultSet_edit.getString("client_id"))))
   {
	  out.println("<option value="+resultSet.getString("client_id")+" > "+resultSet.getString("client_name")+" </option>");
   }else
	 out.println("<option value="+resultSet_edit.getString("client_id")+" selected> "+resultSet.getString("client_name")+" </option>");
		
	
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
<td >Zone/Region : </td>
<td >
<select name="zone_region" style="width: 150px;">
  <option value="0">Select Zones/Region</option>
<%
 try{
  statement=con.createStatement();
  sql ="SELECT zone_id,zone_name FROM device_zones_regions";
  resultSet = statement.executeQuery(sql);
 while(resultSet.next()){
	 if(!(resultSet.getString("zone_id").equals(resultSet_edit.getString("ZONE_REGION_ID"))))
			out.println("<option value="+resultSet.getString("zone_id")+" > "+resultSet.getString("zone_name")+" </option>");
		else
			 out.println("<option value="+resultSet_edit.getString("ZONE_REGION_ID")+" selected> "+resultSet.getString("zone_name")+" </option>");
		
			
	 
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
<td>State :</td>
<td>
<select name="state" style="width: 150px;">
<option value="0" selected> Select State</option>
<%
 try{
  statement=con.createStatement();
  sql ="SELECT state_id,state_name FROM device_states";
  resultSet = statement.executeQuery(sql);
  while(resultSet.next()){
	  if(!(resultSet.getString("state_id").equals(resultSet_edit.getString("state_id"))))
		{
			out.println("<option value="+resultSet.getString("state_id")+" > "+resultSet.getString("state_name")+" </option>");
		}else
			 out.println("<option value="+resultSet_edit.getString("state_id")+" selected> "+resultSet.getString("state_name")+" </option>");
		
			
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
<td>City :</td>
<td>
<select name="city" style="width: 150px;">
<option value="0" selected> Select City</option>
<%
try{
  statement=con.createStatement();
  sql ="SELECT city_id,city_name FROM device_city";
  resultSet = statement.executeQuery(sql);
  while(resultSet.next()){
	  if(!(resultSet.getString("city_id").equals(resultSet_edit.getString("city_id"))))
		{
			out.println("<option value="+resultSet.getString("city_id")+" > "+resultSet.getString("city_name")+" </option>");
		}else
			 out.println("<option value="+resultSet_edit.getString("city_id")+" selected> "+resultSet.getString("city_name")+" </option>");
		
			
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
<td>*Phone No :</td>
<td>
<input type="text" name="phone_no_txt" style="width: 150px;" value="<%=resultSet_edit.getString("DEV_ID")%>" ></td>
</tr>
<tr>
<td valign="top">Panel ID :</td>
<td valign="top">
<input type="text" name=panel_id_text  maxlength="250" style="width: 150px;" value="<%=resultSet_edit.getString("PANEL_ID")%>">
</td></tr>
<tr>
<td valign="top">Address :</td>
<td valign="top">
<input type="text" name="address_txt"  maxlength="500" style="width: 150px;" value="<%=resultSet_edit.getString("ADDRESS")%>">
</td>
</tr>
<tr>
<td valign="top">Ref. Incoming Phones :</td>
<td valign="top">
<select name="ref_incom_phones" style="width: 150px;">
<option value="" selected> Select Phone Nos.</option>
<%
 try{
  statement=con.createStatement();
  sql ="SELECT distinct IN_PHONE_NO FROM vw_ref_phones";
  resultSet = statement.executeQuery(sql);
 while(resultSet.next()){
	   out.println("<option value="+resultSet.getString("IN_PHONE_NO")+" > "+resultSet.getString("IN_PHONE_NO")+" </option>");
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
<td>In-comming Phone (1):</td>
<td><input type="text" name="in_phone_no_1"   style="width: 150px;" value="<%=resultSet_edit.getString("IN_PHONE_NO_1")%>"> <input type="button" name="in_phone_no_1_bt" value="<<"  style="width: 35px;" onclick="document.cr_new_device.in_phone_no_1.value=document.cr_new_device.ref_incom_phones.value"></td>
</tr>
<tr>
<td>In-comming Phone (2):</td>
<td><input type="text" name="in_phone_no_2"   style="width: 150px;" value="<%=resultSet_edit.getString("IN_PHONE_NO_2")%>"> <input type="button" name="in_phone_no_2_bt" value="<<"  style="width: 35px;" onclick="document.cr_new_device.in_phone_no_2.value=document.cr_new_device.ref_incom_phones.value"></td>
</tr>
<tr>
<td>In-comming Phone (3):</td>
<td><input type="text" name="in_phone_no_3"   style="width: 150px;" value="<%=resultSet_edit.getString("IN_PHONE_NO_3")%>"> <input type="button" name="in_phone_no_3_bt" value="<<"  style="width: 35px;" onclick="document.cr_new_device.in_phone_no_3.value=document.cr_new_device.ref_incom_phones.value"></td>
</tr>
<tr>
<td>In-comming Phone (4):</td>
<td><input type="text" name="in_phone_no_4"   style="width: 150px;" value="<%=resultSet_edit.getString("IN_PHONE_NO_4")%>"> <input type="button" name="in_phone_no_4_bt" value="<<"  style="width: 35px;" onclick="document.cr_new_device.in_phone_no_4.value=document.cr_new_device.ref_incom_phones.value"></td>
</tr>
<tr>
<td>In-comming Phone (5):</td>
<td><input type="text" name="in_phone_no_5"   style="width: 150px;" value="<%=resultSet_edit.getString("IN_PHONE_NO_5")%>"> <input type="button" name="in_phone_no_5_bt" value="<<"  style="width: 35px;" onclick="document.cr_new_device.in_phone_no_5.value=document.cr_new_device.ref_incom_phones.value"></td>
</tr>
<tr>
<td>In-comming Phone (6):</td>
<td><input type="text" name="in_phone_no_6"   style="width: 150px;" value="<%=resultSet_edit.getString("IN_PHONE_NO_6")%>"> <input type="button" name="in_phone_no_6_bt" value="<<"  style="width: 35px;" onclick="document.cr_new_device.in_phone_no_6.value=document.cr_new_device.ref_incom_phones.value"></td>
</tr>
<tr>
<td>In-comming Phone (7):</td>
<td><input type="text" name="in_phone_no_7"   style="width: 150px;" value="<%=resultSet_edit.getString("IN_PHONE_NO_7")%>"> <input type="button" name="in_phone_no_7_bt" value="<<"  style="width: 35px;" onclick="document.cr_new_device.in_phone_no_7.value=document.cr_new_device.ref_incom_phones.value"></td>
</tr>
<tr>
<td>In-comming Phone (8):</td>
<td><input type="text" name="in_phone_no_8"   style="width: 150px;" value="<%=resultSet_edit.getString("IN_PHONE_NO_8")%>"> <input type="button" name="in_phone_no_8_bt" value="<<"  style="width: 35px;" onclick="document.cr_new_device.in_phone_no_8.value=document.cr_new_device.ref_incom_phones.value"></td>
</tr>
<tr>
<td>In-comming Phone (9):</td>
<td><input type="text" name="in_phone_no_9"   style="width: 150px;" value="<%=resultSet_edit.getString("IN_PHONE_NO_9")%>"> <input type="button" name="in_phone_no_9_bt" value="<<"  style="width: 35px;" onclick="document.cr_new_device.in_phone_no_9.value=document.cr_new_device.ref_incom_phones.value"></td>
</tr>
<tr>
<td>In-comming Phone (10):</td>
<td><input type="text" name="in_phone_no_10"  style="width: 150px;" value="<%=resultSet_edit.getString("IN_PHONE_NO_10")%>"> <input type="button" name="in_phone_no_10_bt" value="<<"  style="width: 35px;" onclick="document.cr_new_device.in_phone_no_10.value=document.cr_new_device.ref_incom_phones.value"></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td>
<input type="button" Name"add_device" value="Save Device" onclick="save_device()">
&nbsp;&nbsp;
<input type="reset" Name"reset_device" value="Reset">
</td>
<td></td>
</tr>
</table>
<% 
	 }	 
	 connection.close();
 } 
} 
catch (Exception e) {
 e.printStackTrace();
 }
 %>
</form>
</font>
</body>
</html>