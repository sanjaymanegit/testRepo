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
 String condition_str =" DEV_ID > 0";
 
 %>    
     
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Inputs for Reports </title>
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

Offline {
  color: red;
  font-family: Calibri;
  font-size: 90%;
}
</style>
</head>
<body style="font-size:15px">
<font style='font-family="Calibri"'>
<form name="listform">
<%
 String sql ="";
 String status=request.getParameter("status");
 String client_id=request.getParameter("client_name");
 String zone_name=request.getParameter("zone");
 String state_name=request.getParameter("state");
 String city=request.getParameter("city");
 String search_by_phone_no_var=request.getParameter("search_by_phone_no_var");
 String serach_by_phone_no_txt=request.getParameter("serach_by_phone_no_txt");
 String serach_by_panel_id_txt=request.getParameter("serach_by_panel_id_txt");
 String search_by_panel_id_flg=request.getParameter("search_by_panel_id_flg");
 
 if(status != null && !status.trim().isEmpty())
 {
  if(status.length() > 0 )
 	{
 	 condition_str =condition_str + " AND  STATUS_ACTUAL='"+status+"'";  
 	}
 }
 
 if(client_id != null && !client_id.trim().isEmpty())
 {
  if(client_id.length() > 0 )
 	{
 	 condition_str =condition_str + " AND  CLIENT_ID='"+client_id+"'";  
 	}
 }
 
 if(zone_name != null && !zone_name.trim().isEmpty())
 {
  if(zone_name.length() > 0 )
 	{
 	 condition_str =condition_str + " AND  ZONE='"+zone_name+"'";  
 	}
 } 
 
 if(state_name != null && !state_name.trim().isEmpty())
 {
  if(state_name.length() > 0 )
 	{
 	 condition_str =condition_str + " AND  STATE='"+state_name+"'";  
 	}
 } 
 
  if(city != null && !city.trim().isEmpty())
 {
  if(city.length() > 0 )
 	{
 	 condition_str =condition_str + " AND  CITY='"+city+"'";  
 	}
 } 
 
 if(search_by_phone_no_var != null && !search_by_phone_no_var.trim().isEmpty())
 {
  if(serach_by_phone_no_txt.length() > 0 )
 	{
 	 condition_str =condition_str + " AND  DEV_ID='"+serach_by_phone_no_txt+"'";  
 	}
   
 }

 if(search_by_panel_id_flg != null && !search_by_panel_id_flg.trim().isEmpty())
 {
  if(serach_by_panel_id_txt.length() > 0 )
 	{
 	 condition_str =condition_str + " AND  PANEL_ID='"+serach_by_panel_id_txt+"'";  
 	}
 }
 //out.println(" status: "+status+" zone:"+zone_name+"  client_id:"+client_id+" state:"+state_name);
 //out.println(" condition_str "+condition_str);

%>
<table border=0 style="width: 1000px;">
<tr bgcolor="#CFF7EC" >
<td>Phone No</td>
<td>Client Name</td>
<td>Zone/Region</td>
<td>Status</td>
<td>Status Check Date </td>
<td>Panel Id </td>
<td>State</td>
<td>City</td>
<td>Address</td>
</tr>
<%
 try{
  statement=con.createStatement();
  sql ="SELECT  DEV_ID ,CLIENT_NAME, ZONE ,STATE,CITY, ADDRESS, STATUS , L_DATE,PANEL_ID FROM device_status_list where "+condition_str;
  resultSet = statement.executeQuery(sql);
 while(resultSet.next()){
 %>
<tr>
<td><a href = "setup_device.jsp?edit_radio=<%=resultSet.getString("DEV_ID")%>&flag=edit" target="bottomframe2"><%=resultSet.getString("DEV_ID")%></a></td>
<td><%=resultSet.getString("CLIENT_NAME")%></td>
<td><%=resultSet.getString("ZONE")%></td>
<td><%=resultSet.getString("STATUS")%></td>
<td><%=resultSet.getString("L_DATE")%></td> 
<td><%=resultSet.getString("PANEL_ID")%></td> 
<td><%=resultSet.getString("STATE")%></td>
<td><%=resultSet.getString("CITY")%></td>
<td><%=resultSet.getString("ADDRESS")%></td>
</tr>
<%
}
 connection.close();
 } catch (Exception e) {
 e.printStackTrace();
 }
%>
</table>
<%
 try{
  statement=con.createStatement();
  sql ="INSERT INTO device_dtls(DEV_ID) select A.DEV_ID from device_status_list A WHERE A.DEV_ID NOT IN (SELECT DISTINCT B.DEV_ID FROM device_dtls B)";
  statement.executeUpdate(sql);
  connection.close();
   } catch (Exception e) {
 e.printStackTrace();
 }
 %>
</form>
</font>
</body>
</html>