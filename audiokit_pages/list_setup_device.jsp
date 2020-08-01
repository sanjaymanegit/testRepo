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
 %>    
     
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Setup Device Details </title>
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
<script>
function del_rec()
{
	var input_flag = confirm(" Confirm the device which is going to delete : "+document.listform.elements['delete_radio'].value);
	if(input_flag == true)
	{
    document.listform.flag.value="delete";
	document.listform.action="list_setup_device.jsp";
	document.listform.submit();
	}
    
}
function edit_rec()
{	
    //alert(document.listform.elements['edit_radio'].value);
    document.listform.target ="setup_bottom_right_frame";
    document.listform.flag.value="edit";
	document.listform.action="setup_device.jsp";
	document.listform.submit();
	
    
}
</script>
</head>
<body style="font-size:15px">
<font style='font-family="Calibri"'>
<form name="listform">
<% 
String zone_region_id=request.getParameter("zone_region");
String client_id=request.getParameter("client_id");
String search_by_phone_no_var=request.getParameter("search_by_phone_no_var");
String serach_by_phone_no_txt=request.getParameter("serach_by_phone_no_txt");
String condition_str=" A.DEV_ID > 0 ";

if(search_by_phone_no_var != null && !search_by_phone_no_var.trim().isEmpty())
{
 if(serach_by_phone_no_txt.length() > 0 )
	{
	 condition_str =condition_str + " AND  A.DEV_ID='"+serach_by_phone_no_txt+"'";  
	}
}

if(client_id != null && !client_id.trim().isEmpty())
{
 if(client_id.length() > 0 )
	{
	 condition_str =condition_str + " AND  A.CLIENT_ID='"+client_id+"'";  
	}
}

if(zone_region_id != null && !zone_region_id.trim().isEmpty())
{
 if(zone_region_id.length() > 0 )
	{
	 condition_str =condition_str + " AND  A.ZONE_REGION_ID='"+client_id+"'";  
	}
}
//out.println("condition_str :"+condition_str);
%>
<%
 //String zone=request.getParameter("zone");
 String flag=request.getParameter("flag");
 String dev_id=request.getParameter("delete_radio");
if (flag != null)
{	
	if (flag.equals("delete"))	
	{
	//out.println("flag  : "+flag);
	try{	 
		 statement=con.createStatement();
		 String sql_del ="delete FROM device_dtls where dev_id='"+dev_id+"'";;
		 statement.executeUpdate(sql_del);
		 
		 String sql_del2 ="delete FROM device_status where dev_id='"+dev_id+"'";;
		 statement.executeUpdate(sql_del2);
		 
		 //out.println("Record Deleted for Phone no :"+dev_id);
		 connection.close();
		} catch (Exception e)
		{
			e.printStackTrace();
		} 
	}
}
%>
<input type="hidden" name="flag" Value=""">
<table border="0" style="width: 1000px;">
<tr bgcolor="#CFF7EC">
<td><input type="button" name="edit" Value="Edit" onclick="edit_rec()"></td>
<td><input type="button" name="delete" Value="Delete" onclick="del_rec()">
<td>Phone No</td>
<td>Client Name</td>
<td>Address</td>
<td>Zone/Region</td>
<td>State</td>
<td>City</td>
<td>Panel ID</td>
</td>
</tr>
<%
 try{ 
 statement=con.createStatement();
 String sql ="SELECT  A.DEV_ID ,D.STATE_NAME as STATE,E.CITY_NAME as CITY , C.ZONE_NAME as ZONE ,A.ZONE_REGION_ID, A.ADDRESS, B.CLIENT_NAME as CLIENT_NAME,A.PANEL_ID FROM device_dtls A LEFT OUTER JOIN CLIENT_DTLS B ON (A.CLIENT_ID=B.CLIENT_ID) LEFT OUTER JOIN DEVICE_ZONES_REGIONS C ON (A.ZONE_REGION_ID =C.ZONE_ID) LEFT OUTER JOIN DEVICE_STATES D ON (A.STATE_ID=D.STATE_ID) LEFT OUTER JOIN DEVICE_CITY E ON(A.CITY_ID=E.CITY_ID) where "+condition_str; 
 resultSet = statement.executeQuery(sql);
 while(resultSet.next()){
 %>
<tr>
<td><input type="radio" name="edit_radio" value="<%=resultSet.getString("DEV_ID")%>" checked></td>
<td><input type="radio" name="delete_radio" value="<%=resultSet.getString("DEV_ID")%>" checked></td> 
<td><%=resultSet.getString("DEV_ID")%></td>
<td><%=resultSet.getString("CLIENT_NAME")%></td>
<td><%=resultSet.getString("ADDRESS")%></td>
<td><%=resultSet.getString("ZONE")%></td>
<td><%=resultSet.getString("STATE")%></td>
<td><%=resultSet.getString("CITY")%></td>
<td><%=resultSet.getString("PANEL_ID")%></td>
</tr>
<%
}
 connection.close();
 } catch (Exception e) {
 e.printStackTrace();
 }
%>
</table>
</form>
</font>
</body>
</html>