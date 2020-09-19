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
java.sql.Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/fci","root","31@dec2019"); 
Statement st= con.createStatement(); 
 Connection connection = null;
 Statement statement = null;
 Statement statement1 = null; 
 ResultSet resultSet = null;
 ResultSet resultSet_1 = null;
 int record_count=0;
 int rec_key_count=0;	
 String recipe_batch_id = null;
 %> 


<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Insert title here</title>
<script language="JavaScript">
function SelectAll(source)
{
	var checkboxes = document.getElementsByName('chkbox_for_batch');	
	for(c=0; c<=checkboxes.length; c++ )
		{	
		checkboxes[c].checked = source.checked;	
		}
}	

function ShowHiddenVar()
{
	var HiddenStr=''; 
	
	var checkboxes = document.getElementsByName('chkbox_for_batch');	
	for(c=0; c<=checkboxes.length; c++ )
		{			
		
		HiddenStr += HiddenStr+"------------";
		alert(HiddenStr)
		HiddenStr = checkboxes[c].value;
		}	
	;
}

function f_print_rpt()
{
	  document.frm_batch_list.action="BatchDetailsPrint.jsp";
	  document.frm_batch_list.method="post";
	  document.frm_batch_list.submit();
	
}

function poponload()
{
	//alert("device id :"+document.frm_batch_list.device_id.value);    
    testwindow = window.open("", "mywindow", "location=1,status=1,scrollbars=1,width=1150,height=1000");
    document.frm_batch_list.target="mywindow";
    document.frm_batch_list.action="IssueDetailsPrint.jsp";
    document.frm_batch_list.method="post";
    document.frm_batch_list.submit();
    testwindow.moveTo(500, 300);
}

function curr_page_poponload()
{
    testwindow = window.open("", "mywindow", "location=1,status=1,scrollbars=1,width=1150,height=1000");
    document.frm_batch_list.target="mywindow";
    document.frm_batch_list.action="batch_list_print.jsp";
    document.frm_batch_list.method="post";
    document.frm_batch_list.submit();
    testwindow.moveTo(500, 300);
}

function del_fun()
{
	document.frm_batch_list.del_batch_flag.value="Yes"; 
	//document.frm_batch_list.target ="rightbottomframe"; 
    document.frm_batch_list.action="batch_list.jsp";
    document.frm_batch_list.method="post";
    document.frm_batch_list.submit();	
}
</script>
 <style>
body {
  color: black;
  font-family: Verdana, Geneva, sans-serif;
  font-size: 80%;
}
</style>
</head>
<body>
<form name="frm_batch_list" >
<input type="hidden" name="del_batch_flag" value="No">
<%
String from_dt = request.getParameter("from_date_val");
String to_dt = request.getParameter("to_date_val");
String device_id = request.getParameter("device_id");

if(from_dt == null)
{
from_dt ="08/05/2020";	
}
if(to_dt == null)
{
to_dt ="12/31/2020";	
}

if(device_id==null)
{
	device_id="202008/15";
}	

//out.println(" rolename :"+rolename);
//out.println(" to_dt :"+to_dt);
out.println("<input type=hidden name=from_date_val value="+from_dt+">");
out.println("<input type=hidden name=to_date_val value="+to_dt+">");
out.println("<input type=hidden name=device_id value="+device_id+">");

String where_clause = "  a.device_id='"+device_id+"' and a.batch_date between STR_TO_DATE('"+from_dt+"',\"%m/%d/%Y\") and STR_TO_DATE('"+to_dt+"',\"%m/%d/%Y\"))";
try{
statement=con.createStatement();
String sql ="SELECT a.batch_id  FROM batch_mst a ";
resultSet = statement.executeQuery(sql);
//record_count = resultSet.getRow();
while(resultSet.next())
		{
	record_count =record_count+1;
		}
connection.close();
} catch (Exception e) {
e.printStackTrace();
}
//out.println(" record_count :"+record_count);
%>


<table border="0" style="width: 1000px;">
<tbody>
<tr> <td colspan=4><input type="button" value=" Generate Report" onclick="poponload()"><input type="button" value=" Print Report" onclick="curr_page_poponload()" disabled> 
<%
String rolename = request.getParameter("role_name");
out.println("<input type=hidden name=role_name value="+rolename+">");
if(!(rolename == null || (rolename.equals(""))))
	if(rolename.equals("ADMIN"))
	{
	   out.println("<input type=button value=Delete onclick=del_fun() disabled>");
	}   
%>
</td>
</tr>
<tr><td></td></tr>
<tr bgcolor="#CFF7EC">
<td><input type="checkbox" name="select_all" value="select_all" onclick="SelectAll(this)" > Issue. Id </td>
<td>Started On </td>
<td>Released.Bags </td>
<td>Released.Wt.Ton </td>
<td>No.Of Trucks </td>
<td>Status </td>
</tr>

</tr>
<%
if (record_count > 0 )
{	
%>
<%
 try{ 
 statement=con.createStatement(); 
 String sql ="select  ISSUE_ID, COUNT(SERIAL_NO) as TOTAL_TRUCKS, FORMAT(SUM(NET_WEIGHT_VAL),3) as TOTAL_NET_WT, FORMAT(SUM(ACCPTED_BAGS),0) as TOTAL_ACCEPTED_BAGS, substr(MAX(IFNULL(SECOND_WT_CREATED_ON,FIRST_WT_CRTEATED_ON)),0,11) as RELEASE_DATE , substr(MAX(IFNULL(SECOND_WT_CREATED_ON,FIRST_WT_CRTEATED_ON)),11,6) as RELEASE_TIME,MIN(IFNULL(FIRST_WT_CRTEATED_ON,SECOND_WT_CREATED_ON)) as START_DATE , CASE WHEN COUNT(SERIAL_NO) >= AVG(TOTAL_TRUCKS_CNT) THEN 'COMPLETE' ELSE 'IN PROGRESS' END as STATUS,ISSUE_ID from WEIGHT_MST where ISSUE_ID > 0 AND DEVICE_ID='"+device_id+"' AND DATE(IFNULL(FIRST_WT_CRTEATED_ON,SECOND_WT_CREATED_ON)) between STR_TO_DATE('"+from_dt+"',\"%m/%d/%Y\") and STR_TO_DATE('"+to_dt+"',\"%m/%d/%Y\") GROUP BY ISSUE_ID ORDER BY ISSUE_ID desc ";
 //out.println("SQL : "+sql);
 resultSet = statement.executeQuery(sql);
 while(resultSet.next()){
 %>
<tr>
 <td><input type="checkbox" name="chkbox_for_batch" value="<%=resultSet.getString("ISSUE_ID")%>"><%=resultSet.getString("ISSUE_ID")%></td> 
 <td><%=resultSet.getString("START_DATE") %></td> 
<td><%=resultSet.getString("TOTAL_ACCEPTED_BAGS") %></td>
<td><%=resultSet.getString("TOTAL_NET_WT") %> </td>
<td><%=resultSet.getString("TOTAL_TRUCKS") %> </td>
<td><%=resultSet.getString("STATUS") %> </td>

<%
}
 connection.close(); 
 } catch (Exception e) {
 e.printStackTrace();
 }
%>
</tr>
<%
}
else
	out.println("<tr><td colspan=7> No Records Found. </td> </tr>");
%>

 
</tbody>
</table>
</form>
</body>
</html>