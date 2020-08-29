package audiokit;


import java.sql.*;  
import java.util.ArrayList;
import java.util.Date;
import java.util.List;
 
import javax.ws.rs.Consumes;
import javax.ws.rs.GET;
import javax.ws.rs.POST;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;
 
import audiokit.AudioKit;
 
@Path("/feedtxn")
public class loadMessages {
	String phone_nos = null;
	
    @GET
    @Path("ping")
    public String getServerTime() {
        System.out.println("RESTful Service 'MessageService' is running ==> ping");
        return "received ping on "+new Date().toString();
    }
    
    @GET
    @Path("sample")
    @Produces({MediaType.APPLICATION_JSON}) 
    public List<AudioKit> getAllMessages() throws Exception{
        
        List<AudioKit> messages = new ArrayList<>();
        
        AudioKit m = new AudioKit();
        m.setPhoneNo("9855978678");
        messages.add(m);
        
        System.out.println("getAllMessages(): found "+messages.size()+" message(s) on DB");
        
        return messages; //do not use Response object because this causes issues when generating XML automatically
    }
    
    @POST
    @Consumes({MediaType.APPLICATION_JSON})
    @Produces({MediaType.TEXT_PLAIN})
    @Path("/post")
    public String postMessage(AudioKit msg) throws Exception{    	
    	try{  
    		Class.forName("com.mysql.jdbc.Driver");  
    		Connection con=DriverManager.getConnection(  
    		"jdbc:mysql://localhost:3306/audiokit","root","31@dec2019"); 
    	
    		Statement stmt=con.createStatement();  
    		 String sql = "INSERT INTO device_status(DEV_ID) VALUES ("+msg.getPhoneNo()+")";
    		 System.out.println("Inserted records into the table...");
    		 stmt.executeUpdate(sql);
    		// while(rs.next())  
    		//System.out.println(rs.getInt(1)+"  "+rs.getString(2)+"  "+rs.getString(3));  
    			con.close();  
    			}catch(Exception e){ System.out.println(e);}
    	        System.out.println("PhoneNo  = "+msg.getPhoneNo());
        return "ok";
    }
    
    @POST
    @Consumes({MediaType.APPLICATION_JSON})
    @Produces({MediaType.TEXT_PLAIN})
    @Path("/get_incomming_phone_nos")
    
    public String getIncommingNos(AudioKit msg) throws Exception{    	
    	try{  
    		Class.forName("com.mysql.jdbc.Driver");  
    		Connection con=DriverManager.getConnection(  
    		"jdbc:mysql://localhost:3306/audiokit","root","31@dec2019"); 
    	  
    		Statement stmt=con.createStatement();  
    		ResultSet rs = null;
    		 
    		 String sql = "select * from  device_dtls where dev_id = '"+msg.getPhoneNo()+"' and ui_update_status='UI_UPDATED'"; 
    		 System.out.println(" sql :"+sql);
    		 rs=stmt.executeQuery(sql);
    		 while(rs.next()) 
    		 { 
    			 phone_nos = rs.getString(5)+","+rs.getString(9)+","+rs.getString(10)+","+rs.getString(11)+","+rs.getString(12)+","+rs.getString(13)+","+rs.getString(14)+","+rs.getString(15)+","+rs.getString(16)+","+rs.getString(17)+"";
    		     System.out.println(phone_nos);
    		 }
    		   con.close();  
    			}catch(Exception e){ System.out.println(e);}
    	        
    	//System.out.println("PhoneNo  = "+msg.getPhoneNo());
    	if (phone_nos != null) 
    	{
    	try{  
    		Class.forName("com.mysql.jdbc.Driver");  
    		Connection con=DriverManager.getConnection("jdbc:mysql://localhost:3306/audiokit","root","31@dec2019");
    		Statement stmt=con.createStatement();
    	    String sql = "update device_dtls set ui_update_status='' where dev_id = '"+msg.getPhoneNo()+"'"; 
		    stmt.executeUpdate(sql);
		    System.out.println(" Updated  ui_update_status Successfully !!!!!");
		    con.close();  
	    }catch(Exception e){ System.out.println(e);}     
    	}
        return phone_nos;
    }
      
}