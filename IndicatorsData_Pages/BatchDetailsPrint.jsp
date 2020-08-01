<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
  
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Print Batch</title>
<style>
body {
  color: black;
  font-family: Verdana, Geneva, sans-serif;
  font-size: 80%;
}
</style>

<script>
function goBack() {
    window.history.back();
}
function poponload()
{
    testwindow = window.open("BatchDetailsPrint.jsp", "mywindow", "location=1,status=1,scrollbars=1,width=1000,height=1000");
    testwindow.moveTo(800, 300);
}

</script>
</head>
<body>

<form action="BatchDetailsPrint.jsp">
<%@page import="java.sql.DriverManager"%>
<%@page import="java.sql.ResultSet"%>
<%@page import="java.sql.Statement"%>
<%@page import="java.sql.Connection"%>
<%@page import ="java.sql.*" %>
<%@page import ="javax.sql.*" %>
<%
Class.forName("com.mysql.jdbc.Driver"); 
java.sql.Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/indicators_db","root","31@dec2019"); 
Statement st= con.createStatement(); 
int rec_key_count=0;	
String v_dev_id=null;
Connection connection = null;
Statement statement = null;
ResultSet resultSet = null;

 %> 

<p> 
<table border="0" style="width: 1000px;">
<tbody>
<tr>
<%
v_dev_id=request.getParameter("device_id");
try{
 statement=con.createStatement();
 String sql ="SELECT company_name, address FROM device_dtls where device_id_str='"+v_dev_id+"'";
 resultSet = statement.executeQuery(sql);
 while(resultSet.next()){
 %>
 <table border="0" align="left" style="width: 1000px;"><tr bgcolor="#E5E7E9">
 <td colspan=5 width="54%"> <B>Company Name:</B> &nbsp;<%=resultSet.getString("company_name")%> </td> 
 <td colspan=5 width="46%"> <B>Address:</B> &nbsp;<%=resultSet.getString("address")%> </td> 
 </tr>
 <tr >
 <td colspan=5>  </td> 
 <td colspan=5>  </td> 
 </tr>
 <tr >
 <td colspan=5>  </td> 
 <td colspan=5>  </td> 
 </tr>
 <tr >
 <td colspan=5>  </td> 
 <td colspan=5> </td> 
 </tr>
 </table>
<%
}
 connection.close();
 } catch (Exception e) {
 e.printStackTrace();
 }
%>
</tr>
<tr>
</tr>
<%
String BatchIdsArr[]= request.getParameterValues("chkbox_for_batch");
String BatchIDs="";

if(BatchIdsArr != null)
{
%>
<%
for(int i=0; i<BatchIdsArr.length; i++)
{
	 BatchIDs=BatchIdsArr[i];
%> 

<tr><td>
<table border="0" align="left" style="width: 1000px;">
<tbody>
<%

 try{
 
 statement=con.createStatement();
 String sql ="SELECT b.company_name,b.address,a.batch_id,case when length(a.batch_id_from_device) > 19 then substring(a.batch_id_from_device,-4) else a.batch_id_from_device end as batch_id_from_device,date_format(a.batch_created_on,'%d - %b - %Y  %T') as batch_created_on, a.vehicle_no,a.cycle_size,a.work_order_id,a.device_id_str,a.design_mix FROM batch_dtls a, device_dtls b where a.batch_id = '"+BatchIDs+"' and a.device_id_str = b.device_id_str";
 resultSet = statement.executeQuery(sql);
 while(resultSet.next()){
 %>
<tr > <td colspan=5>Batch Id :<%=resultSet.getString("batch_id_from_device")%>
</td>
<td colspan=5>Batch Date :<%=resultSet.getString("batch_created_on")%>
</td>
</tr>
<tr > <td colspan=5>Work Id:<%=resultSet.getString("work_order_id")%> / <%=resultSet.getString("device_id_str")%></td>
<td colspan=5>Design Mix:<%=resultSet.getString("design_mix")%>
</td>
</tr>
<tr > <td colspan=5>Cycle Size (M3):<%=resultSet.getString("cycle_size")%>
</td>
<td colspan=5>Vehicle No:<%=resultSet.getString("vehicle_no")%>
</td>
</tr>
<tr > <td colspan=9> 
</td>
</tr>
<tr > <td colspan=9> 
</td>
</tr>
<%
}
 connection.close();
 } catch (Exception e) {
 e.printStackTrace();
 }
%>
<tr bgcolor="grey">
<td>Recipe</td>
<%
 try{
 statement=con.createStatement();
 String sql ="SELECT col1_key FROM batch_recipe_dtls where batch_id = '"+BatchIDs+"'";
 resultSet = statement.executeQuery(sql);
 while(resultSet.next()){
 %>
<td><%=resultSet.getString("col1_key")%> </td> 
<%
}
 connection.close();
 } catch (Exception e) {
 e.printStackTrace();
 }
%>
</tr>
<tr >
<td>  </td>
<%
 try{

 statement=con.createStatement();
 String sql ="SELECT col1_value FROM batch_recipe_dtls where batch_id =  '"+BatchIDs+"'";
 resultSet = statement.executeQuery(sql);
 while(resultSet.next()){
 %>
<td><%=resultSet.getString("col1_value")%> </td> 
<%
}
 connection.close();
 } catch (Exception e) {
 e.printStackTrace();
 }
%>
</tr>
<tr > <td colspan=11> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
</td>
</tr>
<tr > <td colspan=11> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
</td>
</tr>

<tr bgcolor="grey">
<td>Cycle No.(Time)</td>
<%
 try{  
 statement=con.createStatement(); 
  String sql ="SELECT count(distinct a.col1_key) as cnt FROM batch_recipe_dtls a where a.batch_id =  '"+BatchIDs+"'";;
 resultSet = statement.executeQuery(sql);
  while(resultSet.next()){
 rec_key_count = resultSet.getInt("cnt"); 
  }
 //out.println(" recipe fields count "+rec_key_count);
 connection.close();
 } catch (Exception e) {
 e.printStackTrace();
 }
 %>
 
<%
 try{
 statement=con.createStatement();
 String sql ="SELECT col1_key FROM batch_recipe_dtls where batch_id ='"+BatchIDs+"'";
 resultSet = statement.executeQuery(sql);
 while(resultSet.next()){
 %>
<td><%=resultSet.getString("col1_key")%> </td> 
<%
}
 connection.close();
 } catch (Exception e) {
 e.printStackTrace();
 }
%>
<td> Total </td>
</tr>
<%
 try{
 int cycle_no =0;
 int t=0;
 statement=con.createStatement();
 String sql ="SELECT ifnull(cycle_time,'00:00') as cycle_time,col1_value,col2_value,col3_value,col4_value,col5_value,col6_value,col7_value,col8_value,col9_value,col10_value,col11_value,col12_value FROM batch_cycles_dtls where batch_id = '"+BatchIDs+"'";
 resultSet = statement.executeQuery(sql);
 while(resultSet.next()){	
	 t=0;
	 cycle_no = cycle_no+1;
	 out.println("<tr>");
	 out.println("<td>  "+cycle_no+"       ( "+resultSet.getString("cycle_time")+" )</td>");	 
out.println("<td>"+resultSet.getString("col1_value")+"</td>");
t=t+resultSet.getInt("col1_value");
out.println("<td>"+resultSet.getString("col2_value")+"</td>");
t=t+resultSet.getInt("col2_value");
out.println("<td>"+resultSet.getString("col3_value")+"</td>");
t=t+resultSet.getInt("col3_value");
out.println("<td>"+resultSet.getString("col4_value")+"</td>");
t=t+resultSet.getInt("col4_value");

if(resultSet.getInt("col5_value") >= 0)
{
	if(rec_key_count>6)
	{	
	  t=t+resultSet.getInt("col5_value");
	} 
out.println("<td>"+resultSet.getString("col5_value")+"</td>");	 
} 

if(resultSet.getInt("col6_value") >= 0)
{
	if(rec_key_count>6)
	{	
	  t=t+resultSet.getInt("col6_value");
	}  
out.println("<td>"+resultSet.getString("col6_value")+"</td>");	 
} 

if(resultSet.getInt("col7_value") >= 0)
{
	if(rec_key_count>6)
	{	
      out.println("<td>"+resultSet.getString("col7_value")+"</td>");	 
	}  
} 

if(resultSet.getInt("col8_value") >= 0)
{
	if(rec_key_count>6)
	{	
       out.println("<td>"+resultSet.getString("col8_value")+"</td>");	 
	}   
} 

//if(resultSet.getInt("col9_value") >= 0)
//	 {
//out.println("<td>"+resultSet.getString("col9_value")+"</td>");	 
	// } 
		
//if(resultSet.getInt("col10_value") >= 0)
 //  {
 //out.println("<td>"+resultSet.getString("col10_value")+"</td>");   
 //  }

//if(resultSet.getInt("col11_value") >= 0)
//{
//out.println("<td>"+resultSet.getString("col11_value")+"</td>");   
//}
//if(resultSet.getInt("col12_value") >= 0)
//{
//out.println("<td>"+resultSet.getString("col12_value")+"</td>");   
//}
if(t >= 0)
{	
out.println("<td>"+t+"</td>");
}
else
{	
out.println("<td> 0 </td>");	
}
out.println("</tr>");
%>
<%
}
 connection.close();
 } catch (Exception e) {
 e.printStackTrace();
 }
%>
<tr bgcolor="grey">
<td> Grand Total </td>
<%
 try{
  int j=0; 
 statement=con.createStatement();
 String sql ="SELECT sum(col1_value) as  sum_col1_value,sum(col2_value) as sum_col2_value,sum(col3_value) as sum_col3_value,sum(col4_value) as sum_col4_value ,sum(col5_value) as sum_col5_value,sum(col6_value) as sum_col6_value,sum(col7_value) as sum_col7_value,sum(col8_value) as sum_col8_value,sum(col9_value) as sum_col9_value ,sum(col10_value) as sum_col10_value,sum(col11_value) as sum_col11_value,sum(col12_value) as sum_col12_value FROM batch_cycles_dtls where batch_id ='"+BatchIDs+"'";
 resultSet = statement.executeQuery(sql);
 while(resultSet.next()){

out.println("<td>"+resultSet.getString("sum_col1_value")+"</td>");
j=j+resultSet.getInt("sum_col1_value");
out.println("<td>"+resultSet.getString("sum_col2_value")+"</td>");
j=j+resultSet.getInt("sum_col2_value");
out.println("<td>"+resultSet.getString("sum_col3_value")+"</td>");
j=j+resultSet.getInt("sum_col3_value");
out.println("<td>"+resultSet.getString("sum_col4_value")+"</td>");
j=j+resultSet.getInt("sum_col4_value");

if(resultSet.getInt("sum_col5_value") >= 0)
{
  if(rec_key_count>6)
	{	
	j=j+resultSet.getInt("sum_col5_value");
	}
out.println("<td>"+resultSet.getString("sum_col5_value")+"</td>");
}
if(resultSet.getInt("sum_col6_value") >= 0)
{
  if(rec_key_count>6)
	{	
	j=j+resultSet.getInt("sum_col6_value");
	}
out.println("<td>"+resultSet.getString("sum_col6_value")+"</td>");
}
if(resultSet.getInt("sum_col7_value") >= 0)
{
	if(rec_key_count>6)
	{	
	//j=j+resultSet.getInt("sum_col7_value");	
    out.println("<td>"+resultSet.getString("sum_col7_value")+"</td>");
	}
}
if(resultSet.getInt("sum_col8_value") >= 0)
{
	if(rec_key_count>6)
	{	
	//j=j+resultSet.getInt("sum_col8_value");
    out.println("<td>"+resultSet.getString("sum_col8_value")+"</td>");
	}
}
//if(resultSet.getInt("sum_col9_value") >= 0)
//	 {
//	j=j+resultSet.getInt("sum_col9_value");
//out.println("<td>"+resultSet.getString("sum_col9_value")+"</td>");
//	 }
//if(resultSet.getInt("sum_col10_value") >= 0)
//{
//	j=j+resultSet.getInt("sum_col10_value");	
//out.println("<td>"+resultSet.getString("sum_col10_value")+"</td>");
//}
if(j >= 0)
{	
out.println("<td>"+j+"</td>");
}
else
{
out.println("<td> 0 </td>");	
}
%>
<%
}
 connection.close();
 } catch (Exception e) {
 e.printStackTrace();
 }
%>
</tr>
<tr> 
<td colspan=9> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
</td>
</tr>
<tr > <td colspan=9> 
<B> OPERATOR : </B>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
 &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
 &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
 &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
 <B> APPROVED BY : </B></td>
</tr>
<tr> 
<td colspan=9> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
</td>
<tr> 
<td colspan=9> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
</td>
</tbody>
</table>
</td>
</tr>
<%
}
}
%>

<tr><td>
</td>
</tr>
<tr><td>
</td>
</tr>
<tr><td>
</td>
</tr>
<tbody>
</table>
</p>
</form>

</body>
</html>