package bean;
//import java.util.ArrayList;
import java.util.Date;
//import java.util.List;


import java.sql.*;  

 
import javax.ws.rs.Consumes;
import javax.ws.rs.GET;
import javax.ws.rs.POST;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;

import org.codehaus.jackson.map.ObjectMapper;
import java.io.*;

@Path("/fciServer")
public class weightMst {
	@GET
    @Path("ping")
    public String getServerTime() {
        System.out.println("FCI API is up and running");
        return "FCI API is up and running : "+new Date().toString();
    }	
	
	@POST
    @Path("load_weight_mst")
	@Consumes({MediaType.APPLICATION_JSON})
    @Produces({MediaType.APPLICATION_JSON}) 
    public String getWeightData( WeightData msg) throws Exception{
		
		// Convert msg object ot JSON string 
		// open log file for append and append in file 
		String Input_Json_str=null;
		Input_Json_str="Data Loaded Successfully in weight_mst !!";		
				
		 // Creating Object of ObjectMapper define in Jakson Api 
        ObjectMapper Obj = new ObjectMapper(); 
  
        try { 
  
            //get Oraganisation object as a json string 
            String jsonStr = Obj.writeValueAsString(msg); 
  
            // Displaying JSON String 
            System.out.println(" My JSON STRING is :"+jsonStr); 
            
            //append the log file 
            
            String fileName = "incomming_weights.txt"; 
            try { 
                 BufferedWriter out = new BufferedWriter(new FileWriter(fileName,true)); 
                 out.write(jsonStr+"\n"); 
                 out.close();
            } 
            catch (IOException e) { 
                System.out.println("Exception Occurred" + e); 
            } 
            
        	} 
             catch(Exception e){ System.out.println(e);}
        
        
		Class.forName("com.mysql.jdbc.Driver");  
		Connection con=DriverManager.getConnection("jdbc:mysql://localhost:3306/fci","root","31@dec2019");
		//ResultSet resultSet = null;
		
		try{
	   		 Statement stmt=con.createStatement();
	   		 String sql = "DELETE FROM weight_mst WHERE SERIAL_NO ='"+msg.getSerialNo()+"' and BATCH_ID='"+msg.getBatchId()+"' and DEVICE_ID='"+msg.getDeviceId()+"'";
	   		 stmt.executeUpdate(sql);
		   		
			}catch(Exception e){ System.out.println(e);}	
	    try{
    		 Statement stmt=con.createStatement();  
    		 String sql = "INSERT INTO weight_mst (SERIAL_NO,VEHICLE_NO, MATERIAL_NAME,BATCH_ID, STATUS,FIRST_WEIGHT_MODE, FIRST_WEIGHT_VAL,FIRST_WT_CRTEATED_ON,SECOND_WT_MODE,SECOND_WT_VAL,SECOND_WT_CREATED_ON, "
    		 +"NET_WEIGHT_VAL,WEIGHT_TYPE, ACCPTED_BAGS, AVG_BAG_WT, REMARK, MANNUAL_INS_FLG, DRIVER_IN_OUT,PROPOSED_BAGS,TARGET_STORAGE,CURR_TRUCK_CNT,TOTAL_TRUCKS_CNT,CONTRACTOR_ID,ISSUE_ID,WEIGHING_TYPE,DEVICE_ID)VALUES('"
    		 +msg.getSerialNo()+"','"+msg.getVehicleNo()+"','"+msg.getMaterial()+"','"
    		 +msg.getBatchId()+"','"+msg.getStatus()+"','"+msg.getFirstWeightMode()+"','"
    		 +msg.getFirstWeightVal()
    		 +"',STR_TO_DATE('"+msg.getSecondWeightDt()+"','%Y-%m-%d %T'),'"+msg.getSecondWeightMode()+"','"
    		 +msg.getSecondWeightVal()+"','"+"',STR_TO_DATE('"+msg.getSecondWeightDt()+"', '%Y-%m-%d %T')),'"+msg.getNetWeightVal()+"','"
    		 +msg.getWeighingType()+",'"+msg.getAcceptedBags()+"','"+msg.getAvgBagWt()+"','"+msg.getRemark()+"','"+msg.getManualInsFlag()+"','"
    		 +msg.getDriverInOut()+"','"+msg.getProposedBags()+"','"+msg.getTargetStorage()+"','"+msg.getCurrTruckCount()+"','"
    		 +msg.getTotalTruckCount()+"','"+msg.getContractorId()+"','"+msg.getIssueId()+"','"+msg.getWeighingType()+"','"
    		 +msg.getDeviceId()+"'";    		 
             System.out.println("Insert Weight SQL :" + sql);
    		 stmt.executeUpdate(sql);
    			}catch(Exception e){ System.out.println(e);}
		 con.close();
		//return "Data Loaded Successfully !!";	
		return Input_Json_str;
	}	
	
	
	@POST
    @Path("load_batch_mst")
	@Consumes({MediaType.APPLICATION_JSON})
    @Produces({MediaType.APPLICATION_JSON}) 
    public String getBatchtData( BatchData msg) throws Exception{
		
		// Convert msg object ot JSON string 
		// open log file for append and append in file 
		String Input_Json_str=null;
		Input_Json_str="Data Loaded Successfully in batch_mst !!";		
				
		 // Creating Object of ObjectMapper define in Jakson Api 
        ObjectMapper Obj = new ObjectMapper(); 
  
        try { 
  
            //get Oraganisation object as a json string 
            String jsonStr = Obj.writeValueAsString(msg); 
  
            // Displaying JSON String 
            System.out.println(" My JSON STRING is :"+jsonStr); 
            
            //append the log file 
            
            String fileName = "incomming_batches.txt"; 
            try { 
                 BufferedWriter out = new BufferedWriter(new FileWriter(fileName,true)); 
                 out.write(jsonStr+"\n"); 
                 out.close();
            } 
            catch (IOException e) { 
                System.out.println("Exception Occurred" + e); 
            } 
            
        	} 
             catch(Exception e){ System.out.println(e);}
        
        
		Class.forName("com.mysql.jdbc.Driver");  
		Connection con=DriverManager.getConnection("jdbc:mysql://localhost:3306/fci","root","31@dec2019");
		//ResultSet resultSet = null;
		
		try{
	   		 Statement stmt=con.createStatement();
	   		 String sql = "DELETE FROM batch_mst WHERE BATCH_ID='"+msg.getBatchId()+"' and DEVICE_ID='"+msg.getDeviceId()+"'";
	   		 stmt.executeUpdate(sql);
		   		
			}catch(Exception e){ System.out.println(e);}	
	    try{
    		 Statement stmt=con.createStatement();  
    		 String sql = "INSERT INTO batch_mst (BATCH_ID, BATCH_ID_DISPLAY, BATCH_DATE,ACCPT_WT_KG,ACCPT_BAGS_CNT, RECV_WT_KG, RECV_BAGS_CNT,TL_RECVED, TL_ACCPTED, STORAGE_BAGS, MATERIAL_TYPE, STATUS, WAGON_CNT, REQUIRED_TRUCKS, CONTRACTOR_NAME, DEVICE_ID) values "
    		  +msg.getBatchId()+"','"+msg.getBatchIdDisplay()+"','"
    		  +msg.getBatchDt()+"','"
    		  +msg.getAccpetedWtKg()+"','"+msg.getAcceptedBagsCnt()+"','"+msg.getReceivedWtKg()+"','"
    		  +msg.getReceivedBagsCnt()+"','"+msg.getTLReceived()+"','"+msg.getTLAccepted()+"','"
    		  +msg.getShortageBags()+"','"+msg.getMaterial()+"','"+msg.getStatus()+"','"
    		  +msg.getWagonCnt()+"','"+msg.getRequiredTrucks()+"','"+msg.getContractorName()+"','"
    		  +msg.getAccpetedWtKg()+"','"+msg.getAcceptedBagsCnt()+"','"+msg.getReceivedWtKg()+"','"    						  
    		  +msg.getDeviceId()+"'";    		 
             System.out.println("Insert Batch SQL :" + sql);
    		 stmt.executeUpdate(sql);
    			}catch(Exception e){ System.out.println(e);}
		 con.close();
		//return "Data Loaded Successfully !!";	
		return Input_Json_str;
	}	

}
