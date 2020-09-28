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
    document.frm_batch_list.action="BFSDetailsPrint.jsp";
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
    document.frm_batch_list.action="TL_list.jsp";
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
<tr> <td colspan=4><input type="button" value=" Stacks Details" onclick="poponload()"><input type="button" value=" Print Report" onclick="curr_page_poponload()" disabled> 
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
<td><input type="checkbox" name="select_all" value="select_all" onclick="SelectAll(this)" > Material Name </td>
<td>No.Of.Bags </td>
<td>Net.Weight.Ton </td>
<td>Updated On </td>
<td> </td>
<td></td>
</tr>

</tr>
<%
if (record_count > 0 )
{	
%>
<%
 try{ 
 statement=con.createStatement(); 
 String sql ="SELECT MATERIAL, FORMAT(SUM(BAL_BAGS),0) as BAL_BAGS,FORMAT(SUM(BAL_NET_WT),3) as BAL_NET_WT ,MAX(R_DATE) as R_DATE FROM slots_mst  WHERE DEVICE_ID='"+device_id+"' GROUP BY MATERIAL  ";
 //out.println("SQL : "+sql);
 resultSet = statement.executeQuery(sql);
 while(resultSet.next()){
 %>
<tr>
 <td><input type="checkbox" name="chkbox_for_batch" value="<%=resultSet.getString("MATERIAL")%>"><%=resultSet.getString("MATERIAL")%></td> 
 <td><%=resultSet.getString("BAL_BAGS") %></td> 
<td><%=resultSet.getString("BAL_NET_WT") %></td>
<td><%=resultSet.getString("R_DATE") %> </td>
<td> </td>
<td </td>

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