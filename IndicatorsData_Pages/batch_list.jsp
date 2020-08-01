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
java.sql.Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/indicators_db","root","31@dec2019"); 
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
    document.frm_batch_list.action="BatchDetailsPrint.jsp";
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
	document.frm_batch_list.target ="rightbottomframe"; 
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



//out.println(" rolename :"+rolename);
//out.println(" to_dt :"+to_dt);
out.println("<input type=hidden name=from_date_val value="+from_dt+">");
out.println("<input type=hidden name=to_date_val value="+to_dt+">");
out.println("<input type=hidden name=device_id value="+device_id+">");

String where_clause = " a.batch_id in ( select b.batch_id from  batch_dtls b where b.device_id_str='"+device_id+"' AND DATE(b.batch_created_on) between STR_TO_DATE('"+from_dt+"',\"%m/%d/%Y\") and STR_TO_DATE('"+to_dt+"',\"%m/%d/%Y\"))";
try{
statement=con.createStatement();
String sql ="SELECT a.batch_id  FROM batch_dtls a where "+where_clause;
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
<tr> <td colspan=4><input type="button" value=" Generate Report" onclick="poponload()"><input type="button" value=" Print Report" onclick="curr_page_poponload()"> 
<%
String rolename = request.getParameter("role_name");
out.println("<input type=hidden name=role_name value="+rolename+">");
if(!(rolename == null || (rolename.equals(""))))
	if(rolename.equals("ADMIN"))
	{
	   out.println("<input type=button value=Delete onclick=del_fun()>");
	}   
%>
</td>
</tr>
<tr><td></td></tr>

<%
String del_flag_str = request.getParameter("del_batch_flag");
 //out.println("inside flag ="+del_flag_str);
if(!(del_flag_str == null || (del_flag_str.equals(""))))
	if(del_flag_str.equals("Yes"))
	{	
     //out.println("inside flag Yes");
    String BatchIdsArr[]= request.getParameterValues("chkbox_for_batch");
	String BatchIDs="";
	int j=0;
	if(BatchIdsArr != null)
	{	
      statement=con.createStatement();
      for(int i=0; i<BatchIdsArr.length; i++)
       {
			BatchIDs=BatchIdsArr[i];						
			try
			{							
			j=statement.executeUpdate("DELETE FROM batch_cycles_dtls where batch_id = '"+BatchIDs+"'");
			//out.println("Data is successfully Deleted from  batch_cycles_dtls Table !");
			}
			catch(Exception e)
			{
			System.out.print(e);
			e.printStackTrace();
			}
			
			try
			{							
			j=statement.executeUpdate("DELETE FROM batch_recipe_dtls where batch_id = '"+BatchIDs+"'");
			//out.println("Data is successfully Deleted from  batch_recipe_dtls Table !!");
			}
			catch(Exception e)
			{
			System.out.print(e);
			e.printStackTrace();
			}
			
			try
			{							
			j=statement.executeUpdate("DELETE FROM batch_dtls where batch_id = '"+BatchIDs+"'");
			//out.println("Data is successfully Deleted from  batch_dtls Table !!");
			}
			catch(Exception e)
			{
			System.out.print(e);
			e.printStackTrace();
			}
			
	   }	
	}
	}	
%>	


<tr bgcolor="grey">
<td><input type="checkbox" name="select_all" value="select_all" onclick="SelectAll(this)" > Batch Id </td>
<td>Batch Date </td>
<td>Cycles</td>

<%
 try{ 
 statement=con.createStatement(); 
 String sql ="SELECT max(a.batch_id) as  batch_id FROM batch_dtls a where "+where_clause;
 //out.println("SQL : "+sql);
 
 resultSet = statement.executeQuery(sql);
 while(resultSet.next()){
	 recipe_batch_id=resultSet.getString("batch_id");
}
 connection.close();
 } catch (Exception e) {
 e.printStackTrace();
 }	 
 %>


<%
 try{  
 statement=con.createStatement(); 
  String sql ="SELECT count(a.col1_key) as cnt FROM batch_recipe_dtls a where a.batch_id ='"+recipe_batch_id+"'";
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
  String sql ="SELECT a.col1_key FROM batch_recipe_dtls a where a.batch_id ='"+recipe_batch_id+"'";
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
<td>Total</td>

</tr>
<%
if (record_count > 0 )
{	
%>
<%
 try{ 
 statement=con.createStatement(); 
 String sql ="SELECT a.batch_id, case when length(a.batch_id_from_device) > 19 then substring(a.batch_id_from_device,-4) else a.batch_id_from_device end as batch_id_from_device,date_format(a.batch_created_on,'%d - %b - %Y  %T') as batch_created_on  FROM batch_dtls a where "+where_clause+" order by batch_created_on desc ";
 //out.println("SQL : "+sql);
 
 resultSet = statement.executeQuery(sql);
 while(resultSet.next()){
 %>
<tr>
 <td><input type="checkbox" name="chkbox_for_batch" value="<%=resultSet.getString("batch_id")%>"><%=resultSet.getString("batch_id_from_device")%></td> 
 <td><%=resultSet.getString("batch_created_on") %></td> 
 <%
 int b_id = resultSet.getInt("batch_id");
 int j=0;
 try{
 statement1=con.createStatement();
 String sql_1 ="SELECT count(*) as cycle_cnt,sum(a.col1_value) as  sum_col1_value,sum(a.col2_value) as sum_col2_value,sum(a.col3_value) as sum_col3_value,sum(a.col4_value) as sum_col4_value ,sum(a.col5_value) as sum_col5_value,sum(a.col6_value) as sum_col6_value,sum(a.col7_value) as sum_col7_value,sum(a.col8_value) as sum_col8_value,sum(a.col9_value) as sum_col9_value ,sum(a.col10_value) as sum_col10_value,sum(a.col11_value) as sum_col11_value,sum(a.col12_value) as sum_col12_value FROM batch_cycles_dtls a where a.batch_id ="+b_id+" AND "+where_clause;
 resultSet_1 = statement1.executeQuery(sql_1);
 while(resultSet_1.next())
 {
out.println("<td>"+resultSet_1.getString("cycle_cnt")+"</td>");	 
out.println("<td>"+resultSet_1.getString("sum_col1_value")+"</td>");
j=j+resultSet_1.getInt("sum_col1_value");
out.println("<td>"+resultSet_1.getString("sum_col2_value")+"</td>");
j=j+resultSet_1.getInt("sum_col2_value");
out.println("<td>"+resultSet_1.getString("sum_col3_value")+"</td>");
j=j+resultSet_1.getInt("sum_col3_value");
out.println("<td>"+resultSet_1.getString("sum_col4_value")+"</td>");
j=j+resultSet_1.getInt("sum_col4_value");
if(resultSet_1.getInt("sum_col5_value") >= 0)
{
 if(rec_key_count>6)
	{	
	 j=j+resultSet_1.getInt("sum_col5_value");
	}
out.println("<td>"+resultSet_1.getString("sum_col5_value")+"</td>");
}
if(resultSet_1.getInt("sum_col6_value") >= 0)
{
 if(rec_key_count > 6)
	{
	j=j+resultSet_1.getInt("sum_col6_value");
	}
out.println("<td>"+resultSet_1.getString("sum_col6_value")+"</td>");
}
if(resultSet_1.getInt("sum_col7_value") >= 0)
{
	if(rec_key_count > 6)
	{
	//j=j+resultSet_1.getInt("sum_col7_value");	
     out.println("<td>"+resultSet_1.getString("sum_col7_value")+"</td>");
	} 
}
if(resultSet_1.getInt("sum_col8_value") >= 0)
{
	if(rec_key_count > 6)
	{
	//j=j+resultSet_1.getInt("sum_col8_value");
     out.println("<td>"+resultSet_1.getString("sum_col8_value")+"</td>");
	}
}
//if(resultSet_1.getInt("sum_col9_value") >= 0)
//{
	//j=j+resultSet_1.getInt("sum_col9_value");
//out.println("<td>"+resultSet_1.getString("sum_col9_value")+"</td>");
//}
//if(resultSet_1.getInt("sum_col10_value") >= 0)
//{
	//j=j+resultSet_1.getInt("sum_col10_value");
//out.println("<td>"+resultSet_1.getString("sum_col10_value")+"</td>");
//} 
if(j >= 0)
{	
out.println("<td>"+j+"</td>");
}
else
{
out.println("<td>0</td>");	
}
 }
 //connection.close();
 } catch (Exception e) {
 e.printStackTrace();
 }
%> 
</tr>
<%
}
 connection.close();
 } catch (Exception e) {
 e.printStackTrace();
 }
%>

<tr>
<td colspan=3 align="right"> Grand Total :  </td> 
<%
 try{
  int j=0; 
 statement=con.createStatement();
 String sql ="SELECT sum(a.col1_value) as  sum_col1_value,sum(a.col2_value) as sum_col2_value,sum(a.col3_value) as sum_col3_value,sum(a.col4_value) as sum_col4_value ,sum(a.col5_value) as sum_col5_value,sum(a.col6_value) as sum_col6_value,sum(a.col7_value) as sum_col7_value,sum(a.col8_value) as sum_col8_value,sum(a.col9_value) as sum_col9_value ,sum(a.col10_value) as sum_col10_value,sum(a.col11_value) as sum_col11_value,sum(a.col12_value) as sum_col12_value FROM batch_cycles_dtls a where "+where_clause;
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
	if(rec_key_count > 6)
	{
	//j=j+resultSet.getInt("sum_col7_value");	
    out.println("<td>"+resultSet.getString("sum_col7_value")+"</td>");
	}
}
if(resultSet.getInt("sum_col8_value") >= 0)
{
	if(rec_key_count > 6)
	{
	//j=j+resultSet.getInt("sum_col8_value");
      out.println("<td>"+resultSet.getString("sum_col8_value")+"</td>");
	}  
}

//if(resultSet.getInt("sum_col9_value") >= 0)
//{
 //j=j+resultSet.getInt("sum_col9_value");
 //out.println("<td>"+resultSet.getString("sum_col9_value")+"</td>");
//}
//if(resultSet.getInt("sum_col10_value") >= 0)
//{
 //out.println("<td>"+resultSet.getString("sum_col10_value")+"</td>");
//}

if(j>=0)
{
out.println("<td>"+j+"</td>");
}
else
{
out.println("<td> 0 </td>");	
}
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
	out.println("<tr><td colspan=8> No Records Found. </td> </tr>");
%>

</tbody>
</table>
</form>
</body>
</html>