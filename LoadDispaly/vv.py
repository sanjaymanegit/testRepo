import tempfile 
  
fo = tempfile.NamedTemporaryFile() 
print(fo.name) 
  
fo.close() 