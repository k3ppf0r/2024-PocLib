<%@Page Language="C#"%>
<%Response.Write("hello");System.IO.File.Delete(Request.PhysicalPath);%>