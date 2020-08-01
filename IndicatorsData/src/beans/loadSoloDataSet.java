package beans;

import java.util.ArrayList;
//import java.util.ArrayList;
import java.util.Date;
import java.util.List;


import java.sql.*;  

 
import javax.ws.rs.Consumes;
import javax.ws.rs.GET;
import javax.ws.rs.POST;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;





@Path("/LoadSoloData")
public class loadSoloDataSet {

	@GET
    @Path("ping")
    public String getServerTime() {
        System.out.println("Solo- RESTful WEB service Service 'loadIndicatorDataWS' is running .......");
        return "Solo- received ping on "+new Date().toString();
    }	
	
			
	@POST
    @Path("batch_mst_data")
	@Consumes({MediaType.APPLICATION_JSON})
    @Produces({MediaType.APPLICATION_JSON}) 
    public String getBatchMstData(BatchMstData msg) throws Exception{   		
		Class.forName("com.mysql.jdbc.Driver");  
		Connection con=DriverManager.getConnection("jdbc:mysql://localhost:3306/indicators_db","root","31@dec2019");
		ResultSet resultSet = null;   
		
		try{
   		 Statement stmt=con.createStatement();
   		 String sql = "DELETE FROM batch_dtls WHERE unique_batch_id ='"+msg.getBatchIdFromDevice()+"'";
   		 stmt.executeUpdate(sql);
	   		
		}catch(Exception e){ System.out.println(e);}	
		
		try{
	   		 Statement stmt=con.createStatement();
	   		 String sql = "DELETE FROM batch_recipe_dtls WHERE unique_batch_id ='"+msg.getBatchIdFromDevice()+"'";
	   		 stmt.executeUpdate(sql);
		   		
			}catch(Exception e){ System.out.println(e);}
		
		try{
	   		 Statement stmt=con.createStatement();
	   		 String sql = "DELETE FROM batch_cycles_dtls WHERE unique_batch_id ='"+msg.getBatchIdFromDevice()+"'";
	   		 stmt.executeUpdate(sql);
		   		
			}catch(Exception e){ System.out.println(e);}
		
		
		
	    try{
    		 Statement stmt=con.createStatement();  
    		 String sql = "INSERT INTO batch_dtls (batch_id_from_device,vehicle_no,recipe_no,design_mix,cycle_size,cycle_size_type,work_order_id,device_id_str,unique_batch_id,batch_created_on)VALUES('"+msg.getBatchIdFromDevice()+"','"+msg.getVehicleNo()+"','"+msg.getRecipeNo()+"','"+msg.getDesignMix()+"','"+msg.getCycleSize()+"','"+msg.getCycleSizeType()+"','"+msg.getWorkOrderId()+"','"+msg.getDeviceId()+"','"+msg.getBatchIdFromDevice()+"',STR_TO_DATE('"+msg.getBatchDt()+"', '%Y-%m-%d %T'))";    		 
    		 stmt.executeUpdate(sql);
    			}catch(Exception e){ System.out.println(e);}
	    		
		 con.close();
		return "Yes - BatchMstData";
    }
	
	
	@POST
    @Path("recipe_mst_data")
	@Consumes({MediaType.APPLICATION_JSON})
    @Produces({MediaType.APPLICATION_JSON})
    public String getRecipeMstData(RecipeData msg) throws Exception{   		
		Class.forName("com.mysql.jdbc.Driver");  
		Connection con=DriverManager.getConnection("jdbc:mysql://localhost:3306/indicators_db","root","31@dec2019");
		ResultSet resultSet = null;   
	   
		try{
	   		Statement stmt=con.createStatement();
     		String sql = "INSERT INTO batch_recipe_dtls(recipe_no,col1_key,col1_value,batch_id_device,unique_batch_id)VALUES('"+msg.getRecipeNo()+"','"+msg.getCol1Key()+"','"+msg.getCol1Value()+"','"+msg.getBatchIdFromDevice()+"','"+msg.getBatchIdFromDevice()+"')"; 
	   		stmt.executeUpdate(sql);
	   		System.out.println("Inserterd record in batch_recipe_dtls for index i:");			
	   		}catch(Exception e){ System.out.println(e);}
		
		
		try{
	   		Statement stmt=con.createStatement();	   		 
	   		String sql = "UPDATE batch_recipe_dtls a, batch_dtls b  SET a.batch_id = b.batch_id  WHERE a.batch_id_device =b. batch_id_from_device and a.unique_batch_id=b.unique_batch_id and b.unique_batch_id='"+msg.getBatchIdFromDevice()+"'";  
	   		stmt.executeUpdate(sql);
	   		 System.out.println("updated batch_recipe_dtls for batch_id");
	   		 }catch(Exception e){ System.out.println(e);}
		
		
		 con.close();
		return "Yes - RecipeMstData";
    }
	

	@POST
    @Path("cycle_data")
	@Consumes({MediaType.APPLICATION_JSON})
    @Produces({MediaType.APPLICATION_JSON})
    public String getCycleData(BatchCyclesData msg) throws Exception{   		
		Class.forName("com.mysql.jdbc.Driver");  
		Connection con=DriverManager.getConnection("jdbc:mysql://localhost:3306/indicators_db","root","31@dec2019");
		ResultSet resultSet = null;   
	   
		try{
	   		Statement stmt=con.createStatement();
	   		String sql = "";
	   		 sql = "INSERT INTO batch_cycles_dtls(batch_id_device,col1_value,col2_value,col3_value,col4_value,col5_value,col6_value,col7_value,col8_value,recipe_no,cycle_time,cycle_id_device,unique_batch_id)VALUES('"+msg.getBatchIdFromDevice()+"','"+msg.getCol1Value()+"','"+msg.getCol2Value()+"','"+msg.getCol3Value()+"','"+msg.getCol4Value()+"','"+msg.getCol5Value()+"','"+msg.getCol6Value()+"','"+msg.getCol7Value()+"','"+msg.getCol8Value()+"','"+msg.getRecipeNo()+"','"+msg.getCycleTime()+"','"+msg.getCycleId()+"','"+msg.getBatchIdFromDevice()+"')"; 
	   		 stmt.executeUpdate(sql);
			}catch(Exception e){ System.out.println(e);}
		
		 try{
	   		Statement stmt=con.createStatement();
	   		String sql = "UPDATE batch_cycles_dtls a, batch_dtls b  SET a.batch_id = b.batch_id  WHERE a.batch_id_device =b. batch_id_from_device and a.unique_batch_id=b.unique_batch_id and b.unique_batch_id='"+msg.getBatchIdFromDevice()+"'"; 
	   		 stmt.executeUpdate(sql);
	   		 System.out.println("updated batch_cycles_dtls for batch_id");
	   		 }catch(Exception e){ System.out.println(e);}
		
		 con.close();
		return "Yes - CycleData";
    }	
	
	
	
	
	
}
